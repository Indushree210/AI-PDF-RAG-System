from langchain_community.document_loaders import PyPDFLoader
import os

def load_pdf(pdf_path):
    """
    Load a PDF and return a list of Document objects.
    Each document represents one page.
    """

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"{pdf_path} not found.")

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    return documents


if __name__ == "__main__":

    pdf = "uploads/sample.pdf"

    docs = load_pdf(pdf)

    print(f"Total Pages : {len(docs)}")

    print("\nFirst Page\n")

    print(docs[0].page_content[:1000])

    print("\nMetadata\n")

    print(docs[0].metadata)