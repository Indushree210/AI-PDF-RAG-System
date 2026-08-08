from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

from config import (
    QDRANT_HOST,
    QDRANT_PORT,
    COLLECTION_NAME,
)

VECTOR_SIZE = 384

client = QdrantClient(
    host=QDRANT_HOST,
    port=QDRANT_PORT,
)


def create_collection():
    """
    Create the collection if it doesn't already exist.
    """

    if not client.collection_exists(COLLECTION_NAME):

        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=VECTOR_SIZE,
                distance=Distance.COSINE,
            ),
        )

        print(f"Collection '{COLLECTION_NAME}' created.")

    else:

        print(f"Collection '{COLLECTION_NAME}' already exists.")


def get_client():
    """
    Return the Qdrant client.
    """

    create_collection()

    return client


if __name__ == "__main__":

    create_collection()

    info = client.get_collection(COLLECTION_NAME)

    print("\nCollection Information")

    print(info)