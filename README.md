# 📄 AI-Powered PDF Question Answering System (RAG)

## Overview

This project is a Retrieval-Augmented Generation (RAG) based Question Answering system that allows users to upload one or more PDF documents, index their contents into a Qdrant vector database, and ask natural language questions. The application retrieves the most relevant document chunks using semantic search and generates accurate answers using an OpenRouter Large Language Model (LLM).

---

## Overall Architecture

```
                +----------------------+
                |    Upload PDF(s)     |
                +----------+-----------+
                           |
                           v
                  PDF Loader (LangChain)
                           |
                           v
                  Text Chunking (500 chars)
                           |
                           v
          Sentence Transformer Embeddings
                           |
                           v
                 Qdrant Vector Database
                           |
        User Question ---> Embedding
                           |
                           v
            Similarity Search (Top-K Chunks)
                           |
                           v
          OpenRouter Large Language Model
                           |
                           v
             Answer + Source Citations
```

---

## Libraries Used

- Python 3.11
- Streamlit
- LangChain
- Sentence Transformers
- Qdrant Client
- OpenAI Python SDK
- python-dotenv
- PyPDF
- Transformers
- Torch

---

## Embedding Model Used

**Model:** `sentence-transformers/all-MiniLM-L6-v2`

- Embedding Dimension: **384**
- Used to convert PDF text chunks and user queries into dense vector representations for semantic similarity search.

---

## Assumptions Made

- Uploaded files are valid PDF documents.
- Qdrant server is running locally on **localhost:6333**.
- OpenRouter API key is configured in the `.env` file.
- Internet connection is required for OpenRouter API.
- Users index PDFs before asking questions.
- The system answers only from the retrieved document context.

---

## How to Run the Application

### 1. Clone the Repository

```bash
git clone <repository-url>
cd AI_RAG_Assignment
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Qdrant

```bash
docker run -p 6333:6333 qdrant/qdrant
```

### 5. Configure Environment Variables

Create a `.env` file:

```text
OPENROUTER_API_KEY=your_api_key_here
```

### 6. Run the Application

```bash
streamlit run app.py
```

### 7. Usage

1. Upload one or more PDF files.
2. Click **Index PDFs**.
3. Enter a question.
4. Press **Enter** or click **Get Answer**.
5. View the generated answer along with document citations.

---

**Developed using Streamlit, Qdrant, Hugging Face Sentence Transformers, and OpenRouter.**
