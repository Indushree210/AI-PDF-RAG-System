
# AI-Powered PDF Question Answering System (RAG)

## Overview

This project is a Retrieval-Augmented Generation (RAG) based PDF Question Answering System. It allows users to upload one or more PDF documents, index them into a Qdrant vector database, and ask natural language questions. The system retrieves the most relevant document chunks using semantic search and generates answers using an LLM through OpenRouter.

# 📄 AI-Powered PDF Question Answering System (RAG)

## Overview

This project is a Retrieval-Augmented Generation (RAG) based Question Answering system that allows users to upload one or more PDF documents, index their contents into a Qdrant vector database, and ask natural language questions. The application retrieves the most relevant document chunks using semantic search and generates accurate answers using an OpenRouter Large Language Model (LLM).
>>>>>>> ab1d3ab4538678aaa555254ba65e45da7fdf029e

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
>>>>>>> ab1d3ab4538678aaa555254ba65e45da7fdf029e

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
=======
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
>>>>>>> ab1d3ab4538678aaa555254ba65e45da7fdf029e

---

## Embedding Model Used


**sentence-transformers/all-MiniLM-L6-v2**

- Embedding Dimension: **384**
- Used for semantic document retrieval.

**Model:** `sentence-transformers/all-MiniLM-L6-v2`

- Embedding Dimension: **384**
- Used to convert PDF text chunks and user queries into dense vector representations for semantic similarity search.
>>>>>>> ab1d3ab4538678aaa555254ba65e45da7fdf029e

---

## Assumptions Made


- Uploaded PDFs contain extractable text.
- Qdrant server is running locally on port **6333**.
- OpenRouter API key is configured in the `.env` file.
- Internet connection is available for OpenRouter API calls.

- Uploaded files are valid PDF documents.
- Qdrant server is running locally on **localhost:6333**.
- OpenRouter API key is configured in the `.env` file.
- Internet connection is required for OpenRouter API.
- Users index PDFs before asking questions.
- The system answers only from the retrieved document context.
>>>>>>> ab1d3ab4538678aaa555254ba65e45da7fdf029e

---

## How to Run the Application


### 1. Clone the repository

### 1. Clone the Repository
>>>>>>> ab1d3ab4538678aaa555254ba65e45da7fdf029e

```bash
git clone <repository-url>
cd AI_RAG_Assignment
```


### 2. Install dependencies

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
>>>>>>> ab1d3ab4538678aaa555254ba65e45da7fdf029e

```bash
pip install -r requirements.txt
```


### 3. Start Qdrant

### 4. Start Qdrant
>>>>>>> ab1d3ab4538678aaa555254ba65e45da7fdf029e

```bash
docker run -p 6333:6333 qdrant/qdrant
```


### 4. Configure API key

### 5. Configure Environment Variables
>>>>>>> ab1d3ab4538678aaa555254ba65e45da7fdf029e

Create a `.env` file:

```text

OPENROUTER_API_KEY=your_api_key
```

### 5. Run the application

OPENROUTER_API_KEY=your_api_key_here
```

### 6. Run the Application
>>>>>>> ab1d3ab4538678aaa555254ba65e45da7fdf029e

```bash
streamlit run app.py
```


### 6. Usage

- Upload one or more PDF files.
- Click **Index PDFs**.
- Enter a question.
- Press **Enter** or click **Get Answer**.
- View the generated answer along with document citations.

### 7. Usage

1. Upload one or more PDF files.
2. Click **Index PDFs**.
3. Enter a question.
4. Press **Enter** or click **Get Answer**.
5. View the generated answer along with document citations.

---

**Developed using Streamlit, Qdrant, Hugging Face Sentence Transformers, and OpenRouter.**
>>>>>>> ab1d3ab4538678aaa555254ba65e45da7fdf029e
