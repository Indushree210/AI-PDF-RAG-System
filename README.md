# 📄 AI-Powered PDF Question Answering System (RAG)

## Overview

This project is a Retrieval-Augmented Generation (RAG) based Question Answering System that allows users to upload one or more PDF documents, index their contents into a Qdrant vector database, and ask natural language questions.

The application retrieves the most relevant document chunks using semantic search and generates accurate answers using an OpenRouter Large Language Model (LLM).

---

# Overall Architecture

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
- Qdrant Client
- Sentence Transformers
- Hugging Face Transformers
- OpenAI Python SDK
- OpenRouter API
- PyPDF
- python-dotenv
- Torch

---

## Embedding Model Used

**Model:** `sentence-transformers/all-MiniLM-L6-v2`

- Embedding Dimension: **384**
- Used to convert PDF text chunks and user queries into dense vector representations for semantic similarity search.

---

## Assumptions Made

- Uploaded PDFs contain extractable text.
- Uploaded files are valid PDF documents.
- Qdrant server is running locally on **localhost:6333**.
- OpenRouter API key is configured in the `.env` file.
- Internet connection is required for OpenRouter API.
- Users should index PDFs before asking questions.
- The system answers questions only from the retrieved document context.

---

## How to Run the Application

### 1. Clone the Repository

```bash
git clone https://github.com/Indushree210/AI-PDF-RAG-System.git
cd AI_RAG_Assignment
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Start Qdrant

```bash
docker run -p 6333:6333 qdrant/qdrant
```

### 6. Configure Environment Variables

Create a `.env` file in the project root and add:

```env
OPENROUTER_API_KEY=your_api_key_here
```

### 7. Run the Application

```bash
streamlit run app.py
```

---

## Usage

1. Upload one or more PDF files.
2. Click **Index PDFs**.
3. Enter your question.
4. Click **Get Answer** or press **Enter**.
5. View the generated answer along with the relevant document citations.

---

## Features

- Upload multiple PDF documents.
- Automatic text chunking.
- Semantic search using Qdrant Vector Database.
- Fast document retrieval using Sentence Transformers.
- AI-powered answer generation with OpenRouter LLM.
- Source citations for retrieved answers.
- Interactive Streamlit web interface.

---

## Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Vector Database:** Qdrant
- **Embedding Model:** sentence-transformers/all-MiniLM-L6-v2
- **LLM:** OpenRouter
- **Framework:** LangChain

---

## Project Structure

```text
AI_RAG_Assignment/
│── app.py
│── config.py
│── requirements.txt
│── README.md
│── .env
│── utils/
│── services/
│── uploads/
└── ...
```

---

## Developed By

**Indushree C S**