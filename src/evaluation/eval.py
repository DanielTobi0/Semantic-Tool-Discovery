from __future__ import annotations

from src.store_and_retrieve.retrieval import retrieve_tool_chunks
from src.evaluation.dataset import evaluation_dataset


def run_evaluation(*, top_k: int = 3) -> float:
    success_count = 0

    for item in evaluation_dataset:
        query = item["query"]
        expected_tool = item["expected_tool"]

        retrieved = retrieve_tool_chunks(query, top_k=top_k)
        top_predictions = [tool.tool_name for tool in retrieved]

        if expected_tool in top_predictions:
            success_count += 1
            print(f"✅ PASS: {query}... -> {expected_tool}")
        else:
            print(f"❌ FAIL: {query}... -> Got: {top_predictions}, Expected: {expected_tool}")

    accuracy = (success_count / len(evaluation_dataset)) * 100
    print(f"\nOverall Top-{top_k} Retrieval Accuracy: {accuracy}%")
    return accuracy


# if __name__ == "__main__":
#     run_evaluation(top_k=3)