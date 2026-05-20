__all__ = [
	"RetrievedChunk",
	"ToolChunk",
	"ingest_tools_file",
	"parse_tools_file",
	"retrieve_tool_chunks",
]


def __getattr__(name: str):
	if name in {"ToolChunk", "ingest_tools_file", "parse_tools_file"}:
		from .store import ToolChunk, ingest_tools_file, parse_tools_file

		return {
			"ToolChunk": ToolChunk,
			"ingest_tools_file": ingest_tools_file,
			"parse_tools_file": parse_tools_file,
		}[name]

	if name in {"RetrievedChunk", "retrieve_tool_chunks"}:
		from .retrieve import RetrievedChunk, retrieve_tool_chunks

		return {
			"RetrievedChunk": RetrievedChunk,
			"retrieve_tool_chunks": retrieve_tool_chunks,
		}[name]

	raise AttributeError(f"module {__name__} has no attribute {name}")
