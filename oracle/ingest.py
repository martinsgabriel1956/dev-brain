import argparse
import pathlib
import sys

import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub
from openai import OpenAI
from pypdf import PdfReader

import config
import db
from chunking import chunk_text

openai_client = OpenAI(api_key=config.OPENAI_API_KEY)


def embed_batch(texts: list[str]) -> list[list[float]]:
    response = openai_client.embeddings.create(model=config.EMBEDDING_MODEL, input=texts)
    return [item.embedding for item in response.data]


def extract_epub_text(path: pathlib.Path) -> str:
    book = epub.read_epub(str(path))
    parts = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), "html.parser")
            parts.append(soup.get_text(separator="\n"))
    return "\n\n".join(parts).strip()


def extract_text(path: pathlib.Path) -> str:
    if path.suffix == ".pdf":
        reader = PdfReader(str(path))
        return "\n\n".join(page.extract_text() or "" for page in reader.pages).strip()
    if path.suffix == ".epub":
        return extract_epub_text(path)
    return path.read_text(encoding="utf-8", errors="ignore").strip()


def ingest_file(path: pathlib.Path, root: pathlib.Path) -> int:
    text = extract_text(path)
    if not text:
        return 0

    source = str(path.relative_to(root.parent))
    chunks = chunk_text(text)
    if not chunks:
        return 0

    embeddings = embed_batch(chunks)

    db.delete_by_source(source)
    rows = [
        {"source": source, "content": chunk, "embedding": embedding}
        for chunk, embedding in zip(chunks, embeddings)
    ]
    db.insert_chunks(rows)
    return len(rows)


def iter_source_files(root: pathlib.Path):
    if not root.exists():
        return
    for ext in config.INGESTIBLE_EXTENSIONS:
        for path in root.rglob(f"*{ext}"):
            if path.name in config.EXCLUDED_FILENAMES:
                continue
            yield path


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest wiki/raw content into the oracle vector store")
    parser.add_argument(
        "--source",
        choices=["wiki", "raw", "all"],
        default="all",
        help="Which directory tree to ingest (default: all)",
    )
    args = parser.parse_args()

    roots = []
    if args.source in ("wiki", "all"):
        roots.append(pathlib.Path(config.WIKI_ROOT).resolve())
    if args.source in ("raw", "all"):
        roots.append(pathlib.Path(config.RAW_ROOT).resolve())

    total_files = 0
    total_chunks = 0
    for root in roots:
        for path in iter_source_files(root):
            n = ingest_file(path, root)
            if n:
                print(f"  {path.relative_to(root.parent)}: {n} chunks", file=sys.stderr)
            total_files += 1
            total_chunks += n

    print(f"Ingested {total_files} files, {total_chunks} chunks total.")


if __name__ == "__main__":
    main()
