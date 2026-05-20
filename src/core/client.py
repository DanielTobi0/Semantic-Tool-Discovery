from __future__ import annotations

import weaviate
import weaviate.classes.init as wvc_init
from weaviate.auth import Auth

from .config import load_weaviate_settings


def get_weaviate_client() -> weaviate.WeaviateClient:
    settings = load_weaviate_settings()

    headers: dict[str, str] = {}
    if settings.openai_api_key:
        headers["X-OpenAI-Api-Key"] = settings.openai_api_key

    return weaviate.connect_to_weaviate_cloud(
        cluster_url=settings.url,
        auth_credentials=Auth.api_key(settings.api_key),
        headers=headers,
        additional_config=wvc_init.AdditionalConfig(
            timeout=wvc_init.Timeout(init=60)
        ),
    )
