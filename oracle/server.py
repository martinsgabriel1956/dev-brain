from mcp.server.fastmcp import FastMCP
from openai import OpenAI

import config
import db

mcp = FastMCP("oracle", host="0.0.0.0", port=8000)
openai_client = OpenAI(api_key=config.OPENAI_API_KEY)


@mcp.tool()
def search_wiki(query: str, top_k: int = 5) -> str:
    """Search the personal dev-brain wiki and return the most relevant excerpts with their sources."""
    embedding = openai_client.embeddings.create(
        model=config.EMBEDDING_MODEL, input=query
    ).data[0].embedding

    matches = db.match_documents(embedding, match_count=top_k)
    if not matches:
        return "Nenhum resultado encontrado na wiki para essa consulta."

    parts = [
        f"[{m['source']}] (similaridade: {m['similarity']:.2f})\n{m['content']}"
        for m in matches
    ]
    return "\n\n---\n\n".join(parts)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
