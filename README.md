Core implementation of:
Semantic Tool Discovery for Large Language Models: A Vector-Based Approach to MCP Tool Selection
https://arxiv.org/html/2603.20313v1

## Why This Exists

Loading all tools into LLM context is expensive and noisy.
This repo applies a retrieval-first approach:

- build one semantic document per tool
- store those documents in a vector database
- retrieve only top-K relevant tools per query (default K=3)


## Project Layout

- [tools.py](tools.py): source tool catalog (filesystem, mysql, slack, github, time/weather)
- [src/chunks/store.py](src/chunks/store.py): parsing and ingestion into Weaviate
- [src/chunks/retrieve.py](src/chunks/retrieve.py): hybrid retrieval API
- [src/chunks/__init__.py](src/chunks/__init__.py): public chunk module exports

## How It Works

Each tool is converted to a structured text document:

```text
Tool: <tool_name>
Purpose: <purpose>
Capabilities: <capabilities>
Parameters: <parameters>
```

These documents are indexed in Weaviate collection `McpToolChunks` with metadata:

- `tool_name`
- `server`
- `purpose`
- `capabilities`
- `parameters`
- `source_file`

Retrieval uses Weaviate hybrid search (dense + lexical) and returns top results with score metadata.

## Requirements

- Python 3.14+
- Weaviate Cloud instance
- OpenAI API key for Weaviate text vectorization (`text2vec-openai`)

Install dependencies:

```bash
uv sync
```

## Environment Variables

Set these in `.env` or your shell:

- `WEAVIATE_API_KEY`: Weaviate API key
- `WEAVIATE_URL` or `WEAVIATE_REST_ENDPOINT`: Weaviate cluster URL/host
- `OPENAI_API_KEY`: OpenAI key used by Weaviate vectorizer

## Quick Start

1. Ingest [tools.py](tools.py) into Weaviate:

```bash
uv run python -m src.chunks.store
```

Expected output (example):

```text
Inserted 121 tool chunks from .../tools.py
```

2. Run retrieval demo:

```bash
uv run python -m src.chunks.retrieve
```

Example output:

```text
1. [filesystem] search_files (score=...)
2. [filesystem] search_file_content (score=...)
3. [slack] search_files (score=...)
```

## Programmatic Usage

```python
from src.chunks import ingest_tools_file, retrieve_tool_chunks

# Ingest all tool docs from tools.py
ingest_tools_file("tools.py")

# Retrieve relevant tools for a query
hits = retrieve_tool_chunks(
		"find files in a directory",
		top_k=3,
		alpha=0.65,
)

for hit in hits:
	print(hit.server, hit.tool_name, hit.score)
```
