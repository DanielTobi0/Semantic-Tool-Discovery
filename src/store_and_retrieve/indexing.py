from __future__ import annotations

from pathlib import Path

import weaviate
from weaviate.classes.config import Configure, DataType, Property

from src.core.client import get_weaviate_client
from src.core.config import DEFAULT_COLLECTION
from src.core.models import ToolChunk
from src.store_and_retrieve.parsing import parse_tools_file


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


# if __name__ == "__main__":
#     tools_py = "src/tools.py"
#     count = ingest_tools_file(tools_py)
#     print(f"Inserted {count} tool chunks from {tools_py}")
