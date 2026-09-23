import json

import libsql_client

import config

_client: libsql_client.Client | None = None


def get_client() -> libsql_client.Client:
    global _client
    if _client is None:
        _client = libsql_client.create_client_sync(
            url=config.TURSO_DATABASE_URL, auth_token=config.TURSO_AUTH_TOKEN
        )
    return _client


def delete_by_source(source: str) -> None:
    get_client().execute("DELETE FROM documents WHERE source = ?", [source])


def insert_chunks(rows: list[dict]) -> None:
    if not rows:
        return
    stmts = [
        (
            "INSERT INTO documents (source, content, embedding) VALUES (?, ?, vector32(?))",
            [row["source"], row["content"], json.dumps(row["embedding"])],
        )
        for row in rows
    ]
    get_client().batch(stmts)


def match_documents(embedding: list[float], match_count: int = 5) -> list[dict]:
    vec = json.dumps(embedding)
    rs = get_client().execute(
        """
        SELECT d.source, d.content,
               1 - vector_distance_cos(d.embedding, vector32(?)) AS similarity
        FROM vector_top_k('documents_embedding_idx', vector32(?), ?) AS t
        JOIN documents AS d ON d.rowid = t.id
        ORDER BY similarity DESC
        """,
        [vec, vec, match_count],
    )
    return [
        {"source": row[0], "content": row[1], "similarity": row[2]}
        for row in rs.rows
    ]
