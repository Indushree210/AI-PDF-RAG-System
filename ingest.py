import os
import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, Distance, VectorParams

from config import (
    COLLECTION_NAME,
    QDRANT_HOST,
    QDRANT_PORT,
)

from utils.pdf_loader import load_pdf
from utils.chunker import split_documents
from utils.embeddings import embed_documents


client = QdrantClient(
    host=QDRANT_HOST,
    port=QDRANT_PORT,
)


def create_collection_if_not_exists():

    collections = client.get_collections().collections
    existing = [c.name for c in collections]

    if COLLECTION_NAME not in existing:

        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE,
            ),
        )

        print(f"Collection '{COLLECTION_NAME}' created.")

    else:

        print(f"Collection '{COLLECTION_NAME}' already exists.")


def ingest_pdf(pdf_path, original_filename=None):

    print(f"\nReading: {pdf_path}")

    create_collection_if_not_exists()

    # ----------------------------
    # Load PDF
    # ----------------------------

    documents = load_pdf(pdf_path)

    print(f"Pages Loaded: {len(documents)}")

    # ----------------------------
    # Split
    # ----------------------------

    chunks = split_documents(documents)

    print(f"Total Chunks: {len(chunks)}")

    # ----------------------------
    # Embeddings
    # ----------------------------

    print("Generating embeddings...")

    vectors = embed_documents(chunks)

    print("Embeddings generated.")

    points = []

    for chunk, vector in zip(chunks, vectors):

        points.append(

            PointStruct(

                id=str(uuid.uuid4()),

                vector=vector,

                payload={

                    "text": chunk.page_content,

                    "page": chunk.metadata.get("page", 0),

                    "source": (
                        original_filename
                        if original_filename
                        else os.path.basename(pdf_path)
                    ),

                },
            )
        )

    print("Uploading vectors...")

    client.upsert(

        collection_name=COLLECTION_NAME,

        points=points,

        wait=True,

    )

    info = client.get_collection(COLLECTION_NAME)

    print("\n===================================")
    print("PDF indexed successfully!")
    print(f"Added Chunks : {len(points)}")
    print(f"Total Points : {info.points_count}")
    print("===================================\n")


if __name__ == "__main__":

    pdf_folder = "uploads"

    if not os.path.exists(pdf_folder):
        print("Uploads folder not found.")
        exit()

    pdfs = [
        f
        for f in os.listdir(pdf_folder)
        if f.lower().endswith(".pdf")
    ]

    if not pdfs:
        print("No PDF files found.")
        exit()

    for pdf in pdfs:

        ingest_pdf(
            os.path.join(pdf_folder, pdf),
            pdf,
        )