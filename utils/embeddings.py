import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL

MODEL = None


def get_embedding_model():
    global MODEL

    if MODEL is None:
        MODEL = SentenceTransformer(EMBEDDING_MODEL)

    return MODEL


def embed_text(text):
    model = get_embedding_model()

    embedding = model.encode(
        text,
        normalize_embeddings=True
    )

    return embedding.tolist()


def embed_documents(documents):
    model = get_embedding_model()

    texts = [doc.page_content for doc in documents]

    embeddings = model.encode(
        texts,
        batch_size=32,
        show_progress_bar=True,
        normalize_embeddings=True
    )

    return embeddings.tolist()


if __name__ == "__main__":

    vector = embed_text("Artificial Intelligence")

    print("Embedding Dimension:", len(vector))