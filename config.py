import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenRouter API Key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# OpenRouter Free Model
MODEL_NAME = "openrouter/free"

# Qdrant Configuration
QDRANT_HOST = "localhost"
QDRANT_PORT = 6333
COLLECTION_NAME = "pdf_collection"

# Embedding Model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Folder for uploaded PDFs
UPLOAD_FOLDER = "uploads"