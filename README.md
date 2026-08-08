# AI-Powered PDF Question Answering System (RAG)

## Overview

This project is a Retrieval-Augmented Generation (RAG) based PDF Question Answering System. It allows users to upload one or more PDF documents, index them into a Qdrant vector database, and ask natural language questions. The system retrieves the most relevant document chunks using semantic search and generates answers using an LLM through OpenRouter.

---

## Overall Architecture

User Uploads PDF
        │
        ▼
PDF Loader (LangChain)
        │
        ▼
Text Chunking
(RecursiveCharacterTextSplitter)
        │
        ▼
Sentence Embeddings
(all-MiniLM-L6-v2)
        │
        ▼
Qdrant Vector Database
        │
        ▼
User Question
        │
        ▼
Embedding Generation
        │
        ▼
Similarity Search (Qdrant)
        │
        ▼
Retrieved Context
        │
        ▼
OpenRouter LLM
        │
        ▼
Answer + Citations

---

## Libraries Used

- Python
- Streamlit
- LangChain
- Qdrant Client
- Sentence Transformers
- Hugging Face Transformers
- OpenAI Python SDK
- OpenRouter API
- PyPDF
- python-dotenv

---

## Embedding Model Used

**sentence-transformers/all-MiniLM-L6-v2**

- Embedding Dimension: **384**
- Used for semantic document retrieval.

---

## Assumptions Made

- Uploaded PDFs contain extractable text.
- Qdrant server is running locally on port **6333**.
- OpenRouter API key is configured in the `.env` file.
- Internet connection is available for OpenRouter API calls.

---

## How to Run the Application

### 1. Clone the repository

```bash
git clone <repository-url>
cd AI_RAG_Assignment
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start Qdrant

```bash
docker run -p 6333:6333 qdrant/qdrant
```

### 4. Configure API key

Create a `.env` file:

```text
OPENROUTER_API_KEY=your_api_key
```

### 5. Run the application

```bash
streamlit run app.py
```

### 6. Usage

- Upload one or more PDF files.
- Click **Index PDFs**.
- Enter a question.
- Press **Enter** or click **Get Answer**.
- View the generated answer along with document citations.
