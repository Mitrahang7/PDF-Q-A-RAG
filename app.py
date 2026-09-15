```python
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model_name="openai/gpt-oss-120b",
    temperature=0.3,
    api_key=groq_api_key
)

st.title("PDF RAG Q/A System")

st.write("Upload a PDF and ask questions about it.")

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if uploaded_file:

    # Save uploaded PDF temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Load PDF
    loader = PyMuPDFLoader("temp.pdf")
    documents = loader.load()

    st.success("PDF loaded successfully!")

    st.write("Number of pages:", len(documents))

    # Split documents into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    st.write("Number of chunks:", len(chunks))

    # Create embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create FAISS vector store
    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    st.success("PDF processed and ready for questions!")

    question = st.text_input(
        "Ask a question about your PDF:"
    )

    if question:

        results = vector_store.similarity_search(
            question,
            k=3
        )

        context = "\n\n".join(
            result.page_content
            for result in results
        )

        prompt = f"""
You are a PDF question-answering assistant.

Answer the question using only the information provided in the context.

If the answer cannot be found in the context, say:
"I don't know based on the provided document."

Context:
{context}

Question:
{question}
"""

        response = llm.invoke(prompt)

        st.subheader("Answer")
        st.write(response.content)
```
