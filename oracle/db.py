from supabase import Client, create_client

import config

_client: Client | None = None


def get_client() -> Client:
    global _client
    if _client is None:
        _client = create_client(config.SUPABASE_URL, config.SUPABASE_SERVICE_KEY)
    return _client


def delete_by_source(source: str) -> None:
    get_client().table("documents").delete().eq("source", source).execute()


def insert_chunks(rows: list[dict]) -> None:
    if rows:
        get_client().table("documents").insert(rows).execute()


def match_documents(embedding: list[float], match_count: int = 5) -> list[dict]:
    result = get_client().rpc(
        "match_documents",
        {"query_embedding": embedding, "match_count": match_count},
    ).execute()
    return result.data or []
