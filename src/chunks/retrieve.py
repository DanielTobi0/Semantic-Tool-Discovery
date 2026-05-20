from __future__ import annotations

from dataclasses import dataclass

from weaviate.classes.query import Filter, MetadataQuery

from .store import DEFAULT_COLLECTION, get_weaviate_client


@dataclass(slots=True)
class RetrievedChunk:
	tool_name: str
	server: str
	text: str
	purpose: str
	score: float | None
	distance: float | None


def retrieve_tool_chunks(
	query: str,
	*,
	top_k: int = 3,
	alpha: float = 0.65,
	server: str | None = None,
	score_threshold: float | None = None,
	collection_name: str = DEFAULT_COLLECTION,
) -> list[RetrievedChunk]:
	"""
	Hybrid retrieval (dense + lexical) with K=3 default, following the paper's
	recommended operating point and optional threshold filtering.
	"""
	client = get_weaviate_client()
	try:
		collection = client.collections.get(collection_name)
		where_filter = Filter.by_property("server").equal(server) if server else None

		result = collection.query.hybrid(
			query=query,
			alpha=alpha,
			limit=top_k,
			filters=where_filter,
			return_metadata=MetadataQuery(score=True, distance=True),
		)

		rows: list[RetrievedChunk] = []
		for obj in result.objects:
			props = obj.properties
			score = obj.metadata.score if obj.metadata else None

			if score_threshold is not None and (score is None or score < score_threshold):
				continue

			rows.append(
				RetrievedChunk(
					tool_name=str(props.get("tool_name", "")),
					server=str(props.get("server", "")),
					text=str(props.get("text", "")),
					purpose=str(props.get("purpose", "")),
					score=score,
					distance=obj.metadata.distance if obj.metadata else None,
				)
			)

		# Graceful degradation: if threshold removes all items, fall back to top-K.
		if score_threshold is not None and not rows:
			return retrieve_tool_chunks(
				query,
				top_k=top_k,
				alpha=alpha,
				server=server,
				score_threshold=None,
				collection_name=collection_name,
			)

		return rows
	finally:
		client.close()


if __name__ == "__main__":
	sample_query = "I need to search files in a directory"
	retrieved = retrieve_tool_chunks(sample_query, top_k=3)
	for idx, item in enumerate(retrieved, start=1):
		print(f"{idx}. [{item.server}] {item.tool_name} (score={item.score})")
