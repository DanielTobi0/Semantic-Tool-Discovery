# Semantic Tool Discovery for MCP

This project parses the static MCP tool catalog in [src/tools.py](src/tools.py), converts each tool into a semantic document, stores those documents in Weaviate, and retrieves the most relevant tools for a user query.

The notebook [entry_point.ipynb](entry_point.ipynb) is the current entry point. It demonstrates the full flow:
1. ingest the tool catalog into Weaviate,
2. run a sample retrieval query, and
3. evaluate retrieval quality against the built-in dataset.

The implementation is inspired by:
Semantic Tool Discovery for Large Language Models: A Vector-Based Approach to MCP Tool Selection
https://arxiv.org/html/2603.20313v1

## What It Does

- Parses tool definitions from [src/tools.py](src/tools.py)
- Builds one searchable text document per tool
- Stores tool chunks in the `McpToolChunks` Weaviate collection
- Uses hybrid retrieval to return the top-K most relevant tools for a query
- Provides a small evaluation loop to measure top-K retrieval success

## How The Entry Notebook Works

The notebook uses the ingestion, retrieval, and evaluation modules directly. The package also exposes convenience exports from [src/__init__.py](src/__init__.py).

```python
from src.store_and_retrieve.indexing import ingest_tools_file
from src.store_and_retrieve.retrieval import retrieve_tool_chunks
from src.evaluation.eval import run_evaluation
```

Its three cells do the following:

1. Ingest [src/tools.py](src/tools.py) into Weaviate with `ingest_tools_file("src/tools.py")`
2. Query the store with `retrieve_tool_chunks(sample_query, top_k=3)`
3. Run the evaluation suite with `run_evaluation(top_k=3)`

## Data Model

Each tool chunk is stored as a structured text document with this shape:

```text
Tool: <tool_name>
Purpose: <purpose>
Capabilities: <capabilities>
Parameters: <parameters>
```

Only three properties are stored in Weaviate:

- `text`
- `tool_name`
- `server`

The `purpose`, `capabilities`, and `parameters` fields are embedded into `text` to improve retrieval quality.

## Repository Layout

- [src/tools.py](src/tools.py): static MCP tool catalog grouped by server
- [src/core/](src/core): shared configuration, client, and dataclasses
  - [src/core/config.py](src/core/config.py): environment loading and collection name
  - [src/core/client.py](src/core/client.py): Weaviate client factory
  - [src/core/models.py](src/core/models.py): `ToolChunk` and `RetrievedChunk`
- [src/store_and_retrieve/](src/store_and_retrieve): parsing, ingestion, and retrieval
  - [src/store_and_retrieve/parsing.py](src/store_and_retrieve/parsing.py): AST-based tool parser
  - [src/store_and_retrieve/indexing.py](src/store_and_retrieve/indexing.py): collection creation and ingestion
  - [src/store_and_retrieve/retrieval.py](src/store_and_retrieve/retrieval.py): hybrid retrieval API
- [src/evaluation/](src/evaluation): query dataset and evaluation runner

Compatibility exports are available from [src/__init__.py](src/__init__.py).

## Requirements

- Python 3.10+
- Weaviate Cloud or a compatible Weaviate instance
- `OPENAI_API_KEY` for Weaviate text vectorization

Install dependencies with:

```bash
uv sync
```

## Environment Variables

Set these in `.env` or your shell:

- `WEAVIATE_API_KEY`: Weaviate API key
- `WEAVIATE_URL` or `WEAVIATE_REST_ENDPOINT`: Weaviate cluster URL
- `OPENAI_API_KEY`: OpenAI API key used by the Weaviate vectorizer

## Usage

Open [entry_point.ipynb](entry_point.ipynb) and run the cells in order.

To do the same from Python:

```python
from src import ingest_tools_file, retrieve_tool_chunks
from src.evaluation.eval import run_evaluation

count = ingest_tools_file("src/tools.py")
print(f"Inserted {count} tool chunks")

hits = retrieve_tool_chunks("I need to search files in a directory", top_k=3)
for item in hits:
    print(item.server, item.tool_name, item.score)

run_evaluation(top_k=3)
```

Typical ingestion output looks like:

```text
Inserted 121 tool chunks from src/tools.py
```

Typical evaluation output looks like:

```text
✅ PASS: Copy the entire 'images' folder over to ... -> copy_directory
❌ FAIL: When was the database.sqlite file last m... -> Got: ['select_database', 'ping_database', 'disconnect_database'], Expected: get_file_info
```

## Retrieval Defaults

- `top_k=3`: default retrieval depth used in the notebook and evaluation loop
- `alpha=0.65`: hybrid search blend between lexical and semantic matching
- `score_threshold`: optional filter that falls back to top-K if it filters everything out

## Troubleshooting

- Weaviate connection errors: verify `WEAVIATE_API_KEY` and `WEAVIATE_URL`, and confirm network access to the cluster
- Empty retrieval results: run ingestion again and confirm `McpToolChunks` exists
- Vectorizer failures: verify `OPENAI_API_KEY` is set and valid
