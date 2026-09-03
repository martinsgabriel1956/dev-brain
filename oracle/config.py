import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_SERVICE_KEY = os.environ["SUPABASE_SERVICE_KEY"]

EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_DIMENSIONS = 1536

CHUNK_SIZE_TOKENS = 500
CHUNK_OVERLAP_TOKENS = 50

# Meta/navigation files with no standalone knowledge content — excluded from ingestion.
EXCLUDED_FILENAMES = {"log.md", "index.md"}

INGESTIBLE_EXTENSIONS = {".md", ".pdf", ".epub"}

WIKI_ROOT = os.path.join(os.path.dirname(__file__), "..", "wiki")
RAW_ROOT = os.path.join(os.path.dirname(__file__), "..", "raw")
