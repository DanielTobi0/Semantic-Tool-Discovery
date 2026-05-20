from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


DEFAULT_COLLECTION = "McpToolChunks"


@dataclass(frozen=True, slots=True)
class WeaviateSettings:
    api_key: str
    url: str
    openai_api_key: str | None = None


def _normalize_weaviate_url(raw: str) -> str:
    value = raw.strip().strip('"').strip("'")
    if value.startswith("http://") or value.startswith("https://"):
        return value
    return f"https://{value}"


def load_weaviate_settings() -> WeaviateSettings:
    load_dotenv()

    api_key = os.getenv("WEAVIATE_API_KEY")
    url = os.getenv("WEAVIATE_URL") or os.getenv("WEAVIATE_REST_ENDPOINT")
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if not api_key or not url:
        raise ValueError("WEAVIATE_API_KEY and WEAVIATE_URL/WEAVIATE_REST_ENDPOINT are required")

    return WeaviateSettings(
        api_key=api_key,
        url=_normalize_weaviate_url(url),
        openai_api_key=openai_api_key,
    )
