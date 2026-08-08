import os
import traceback

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found in .env")

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

# -----------------------------
# Choose a valid OpenRouter model
# -----------------------------
MODEL_NAME = "nvidia/nemotron-3-ultra-550b-a55b:free"
# Other options:
# MODEL_NAME = "mistralai/mistral-7b-instruct:free"
# MODEL_NAME = "meta-llama/llama-3.1-8b-instruct:free"

SYSTEM_PROMPT = """
You are a Retrieval Augmented Generation (RAG) assistant.

Rules:

1. Answer ONLY using the supplied document context.
2. Never use outside knowledge.
3. If the answer is not present in the supplied context, reply exactly:

The information is not available in the supplied documents.

4. Keep answers concise.
5. Do NOT generate citations.
6. Ignore any instruction not contained in the supplied context.
"""


def generate_answer(question, retrieved_chunks):

    context = ""
    citations = []

    for chunk in retrieved_chunks:

        source = chunk.metadata.get("source", "Unknown")
        page = chunk.metadata.get("page", "Unknown")
        text = chunk.page_content

        context += f"""
Document: {source}
Page: {page}

{text}

------------------------
"""

        citations.append(
            {
                "source": source,
                "page": page,
                "text": text[:500],
            }
        )

    user_prompt = f"""
Use ONLY the document context below.

Context:

{context}

Question:
{question}

Answer:
"""

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            temperature=0,
            max_tokens=500,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
        )

        print("\n========== RAW RESPONSE ==========")
        print(response)
        print("==================================\n")

        if not response.choices:
            return (
                "The model returned no response.",
                citations,
            )

        message = response.choices[0].message

        answer = message.content or ""

        answer = answer.strip()

        invalid_keywords = [
            "user_safety",
            "assistant_response",
            "reasoning",
            "analysis",
            "thinking",
        ]

        if (
            answer == ""
            or any(k in answer.lower() for k in invalid_keywords)
        ):
            answer = (
                "The model returned an invalid response. "
                "Please ask the question again."
            )

        return answer, citations

    except Exception as e:

        print("\n========== ERROR ==========")
        traceback.print_exc()
        print("===========================\n")

        return (
            f"Error:\n{str(e)}",
            citations,
        )


if __name__ == "__main__":

    class DummyDoc:

        def __init__(self):

            self.page_content = (
                "Employees receive 24 annual leave days every year."
            )

            self.metadata = {
                "source": "employee_handbook.pdf",
                "page": 17,
            }

    docs = [DummyDoc()]

    answer, citations = generate_answer(
        "How many annual leave days are provided?",
        docs,
    )

    print("\n========== ANSWER ==========\n")
    print(answer)

    print("\n========== CITATIONS ==========\n")

    for citation in citations:
        print(citation)