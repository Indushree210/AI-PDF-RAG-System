from dataclasses import dataclass

from config import COLLECTION_NAME
from vector_db import get_client
from utils.embeddings import embed_text
from llm import generate_answer

client = get_client()


@dataclass
class Document:
    page_content: str
    metadata: dict


def retrieve_documents(question, limit=5):

    query_vector = embed_text(question)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=limit,
    ).points

    retrieved = []

    print("\n========== RETRIEVED DOCUMENTS ==========\n")

    for point in results:

        payload = point.payload

        text = payload["text"].replace("\n", " ")

        print(f"Source : {payload['source']}")
        print(f"Page   : {payload['page']}")
        print(f"Text   : {text[:300]}")
        print("-" * 80)

        retrieved.append(
            Document(
                page_content=payload["text"],
                metadata={
                    "source": payload["source"],
                    "page": payload["page"],
                },
            )
        )

    return retrieved


def ask(question):

    docs = retrieve_documents(question)

    answer, citations = generate_answer(
        question,
        docs,
    )

    return answer, citations


if __name__ == "__main__":

    while True:

        question = input("\nQuestion (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        answer, citations = ask(question)

        print("\n========== ANSWER ==========\n")
        print(answer)

        print("\n========== CITATIONS ==========\n")

        for c in citations:
            print(c)