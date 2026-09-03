import tiktoken

import config

_encoding = tiktoken.get_encoding("cl100k_base")


def chunk_text(text: str) -> list[str]:
    tokens = _encoding.encode(text)
    if not tokens:
        return []

    chunks = []
    step = config.CHUNK_SIZE_TOKENS - config.CHUNK_OVERLAP_TOKENS
    for start in range(0, len(tokens), step):
        window = tokens[start : start + config.CHUNK_SIZE_TOKENS]
        chunks.append(_encoding.decode(window))
        if start + config.CHUNK_SIZE_TOKENS >= len(tokens):
            break
    return chunks
