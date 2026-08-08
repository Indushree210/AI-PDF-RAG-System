from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils.pdf_loader import load_pdf
import os


def split_documents(documents):
    """
    Split PDF documents into smaller chunks while preserving metadata.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    for doc in documents:
        text = doc.page_content
        

    # Remove common header/footer
    text = text.replace("Copyright @ Manupatra 2024-2025", "")
    text = text.replace("Manupatra", "")

    doc.page_content = text

    chunks = text_splitter.split_documents(documents)

    return chunks


if __name__ == "__main__":

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pdf_path = os.path.join(BASE_DIR, "uploads", "sample.pdf")

    docs = load_pdf(pdf_path)

    chunks = split_documents(docs)

    print(f"Original Pages: {len(docs)}")
    print(f"Total Chunks: {len(chunks)}")

    print("\nFirst Chunk:\n")
    print(chunks[0].page_content)

    print("\nMetadata:\n")
    print(chunks[0].metadata)