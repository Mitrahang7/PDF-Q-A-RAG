# PDF Q&A RAG

A Retrieval-Augmented Generation (RAG) application that allows users to upload a PDF and ask questions about its content using semantic search and a Large Language Model (LLM).

This project was built to understand the complete RAG pipeline, from PDF text extraction and chunking to embeddings, vector search, retrieval, and LLM-based answer generation.

## Live Demo

**Streamlit App:**
(https://pdf-q-a-rag-blfnzx8ntdknqvrl8urdbd.streamlit.app/)

## Features

* Upload a PDF document
* Extract text from PDF pages
* Split documents into smaller chunks
* Generate embeddings using Hugging Face
* Store embeddings using FAISS
* Perform semantic similarity search
* Generate answers using a Groq-hosted LLM
* Ask questions about the uploaded document

## RAG Pipeline

```text
PDF
 ↓
PyMuPDF
 ↓
Text Extraction
 ↓
Text Chunking
 ↓
Hugging Face Embeddings
 ↓
FAISS
 ↓
Similarity Search
 ↓
Relevant Chunks
 ↓
Context
 ↓
Groq LLM
 ↓
Answer
```

## Tech Stack

* Python
* Streamlit
* LangChain
* PyMuPDF
* RecursiveCharacterTextSplitter
* Hugging Face
* Sentence Transformers
* FAISS
* Groq
* python-dotenv

## How It Works

### 1. PDF Upload

The user uploads a PDF through the Streamlit interface.

### 2. Text Extraction

PyMuPDF is used to extract text from the uploaded PDF.

### 3. Text Chunking

The extracted text is divided into smaller overlapping chunks using `RecursiveCharacterTextSplitter`.

This allows the retrieval system to find more relevant sections of the document when answering a question.

### 4. Embeddings

Each text chunk is converted into a numerical vector using:

```text
sentence-transformers/all-MiniLM-L6-v2
```

These vectors represent the semantic meaning of the text.

### 5. Vector Storage

The generated embeddings are stored in a FAISS vector store.

FAISS allows the application to search for chunks that are semantically similar to the user's question.

### 6. Retrieval

When the user asks a question, the system searches FAISS and retrieves the most relevant document chunks.

### 7. Generation

The retrieved chunks are provided as context to the LLM through Groq.

The LLM generates an answer based on the retrieved information.

## Installation

### Clone the Repository

```bash
git clone https://github.com/Mitrahang7/PDF-Q-A-RAG.git
```

```bash
cd PDF-Q-A-RAG
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

The `.env` file should never be committed to GitHub.

## Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.



## Project Structure

```text
PDF-Q-A-RAG/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore

```




The project helped me understand how an LLM can generate answers using information retrieved from an external knowledge source rather than relying only on its pretrained knowledge.

## Future Improvements

* Add source page references to answers
* Improve the chat interface
* Improve document processing
* Add conversation history
* Improve retrieval quality
* Refactor the application into separate modules
* Add support for additional document formats
* Improve deployment and application performance

## Author

Mitrahang Limbu

