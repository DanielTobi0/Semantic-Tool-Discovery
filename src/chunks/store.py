from __future__ import annotations

import ast
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
import weaviate
from weaviate.auth import Auth
from weaviate.classes.config import Configure, DataType, Property


DEFAULT_COLLECTION = "McpToolChunks"


@dataclass(slots=True)
class ToolChunk:
	tool_name: str
	server: str
	purpose: str
	capabilities: str
	parameters: str
	source_file: str

	@property
	def text(self) -> str:
		# Paper-aligned document template with strong semantic anchors.
		return (
			f"Tool: {self.tool_name}\n"
			f"Purpose: {self.purpose}\n"
			f"Capabilities: {self.capabilities}\n"
			f"Parameters: {self.parameters}"
		)


def _normalize_weaviate_url(raw: str) -> str:
	value = raw.strip().strip('"').strip("'")
	if value.startswith("http://") or value.startswith("https://"):
		return value
	return f"https://{value}"


def _safe_extract_str(dct: dict[str, Any], key: str) -> str:
	value = dct.get(key, "")
	return value if isinstance(value, str) else str(value)


def parse_tools_file(tools_file: str | Path) -> list[ToolChunk]:
	path = Path(tools_file)
	source = path.read_text(encoding="utf-8")
	tree = ast.parse(source)

	chunks: list[ToolChunk] = []

	for node in tree.body:
		if not isinstance(node, ast.Assign):
			continue
		if len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
			continue

		var_name = node.targets[0].id
		if not var_name.endswith("_mcp_tools"):
			continue

		server_name = var_name.removesuffix("_mcp_tools")
		try:
			tools_dict = ast.literal_eval(node.value)
		except Exception as exc:  # pragma: no cover
			raise ValueError(f"Unable to parse tools from {var_name}") from exc

		if not isinstance(tools_dict, dict):
			continue

		for tool_key, tool_spec in tools_dict.items():
			if not isinstance(tool_key, str) or not isinstance(tool_spec, dict):
				continue

			chunks.append(
				ToolChunk(
					tool_name=_safe_extract_str(tool_spec, "Tool") or tool_key,
					server=server_name,
					purpose=_safe_extract_str(tool_spec, "Purpose"),
					capabilities=_safe_extract_str(tool_spec, "Capabilities"),
					parameters=_safe_extract_str(tool_spec, "Parameters"),
					source_file=str(path),
				)
			)

	return chunks


def get_weaviate_client() -> weaviate.WeaviateClient:
	load_dotenv()

	api_key = os.getenv("WEAVIATE_API_KEY")
	url = os.getenv("WEAVIATE_URL") or os.getenv("WEAVIATE_REST_ENDPOINT")
	openai_api_key = os.getenv("OPENAI_API_KEY")

	if not api_key or not url:
		raise ValueError("WEAVIATE_API_KEY and WEAVIATE_URL/WEAVIATE_REST_ENDPOINT are required")

	headers: dict[str, str] = {}
	if openai_api_key:
		headers["X-OpenAI-Api-Key"] = openai_api_key

	return weaviate.connect_to_weaviate_cloud(
		cluster_url=_normalize_weaviate_url(url),
		auth_credentials=Auth.api_key(api_key),
		headers=headers,
	)


def ensure_collection(
	client: weaviate.WeaviateClient,
	collection_name: str = DEFAULT_COLLECTION,
	recreate: bool = False,
) -> None:
	exists = client.collections.exists(collection_name)
	if exists and recreate:
		client.collections.delete(collection_name)
		exists = False

	if not exists:
		client.collections.create(
			name=collection_name,
			vectorizer_config=Configure.Vectorizer.text2vec_openai(
				model="text-embedding-3-small"
			),
			properties=[
				Property(name="text", data_type=DataType.TEXT),
				Property(name="tool_name", data_type=DataType.TEXT),
				Property(name="server", data_type=DataType.TEXT),
				Property(name="purpose", data_type=DataType.TEXT),
				Property(name="capabilities", data_type=DataType.TEXT),
				Property(name="parameters", data_type=DataType.TEXT),
				Property(name="source_file", data_type=DataType.TEXT),
			],
		)


def store_tool_chunks(
	client: weaviate.WeaviateClient,
	chunks: list[ToolChunk],
	collection_name: str = DEFAULT_COLLECTION,
) -> int:
	collection = client.collections.get(collection_name)

	inserted = 0
	with collection.batch.dynamic() as batch:
		for chunk in chunks:
			batch.add_object(
				properties={
					"text": chunk.text,
					"tool_name": chunk.tool_name,
					"server": chunk.server,
					"purpose": chunk.purpose,
					"capabilities": chunk.capabilities,
					"parameters": chunk.parameters,
					"source_file": chunk.source_file,
				}
			)
			inserted += 1
	return inserted


def ingest_tools_file(
	tools_file: str | Path,
	collection_name: str = DEFAULT_COLLECTION,
	recreate_collection: bool = False,
) -> int:
	chunks = parse_tools_file(tools_file)
	if not chunks:
		raise ValueError(f"No tool chunks parsed from {tools_file}")

	client = get_weaviate_client()
	try:
		ensure_collection(
			client=client,
			collection_name=collection_name,
			recreate=recreate_collection,
		)
		return store_tool_chunks(client=client, chunks=chunks, collection_name=collection_name)
	finally:
		client.close()


if __name__ == "__main__":
	repo_root = Path(__file__).resolve().parents[2]
	tools_py = repo_root / "tools.py"
	count = ingest_tools_file(tools_py)
	print(f"Inserted {count} tool chunks from {tools_py}")
