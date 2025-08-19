# build_vector_store.py

import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# --- Configuration ---
KNOWLEDGE_BASE_DIR = "knowledge_base"
VECTOR_STORE_PATH = "vector_store.faiss"
EMBEDDING_MODEL = "all-MiniLM-L6-v2" # A good starting model

def build_vector_store():
    """
    Builds a FAISS vector store from documents in the knowledge base directory.

    This function performs the following steps:
    1. Loads documents from the specified directory.
    2. Splits the documents into smaller chunks for effective processing.
    3. Generates embeddings for each chunk using a sentence transformer model.
    4. Creates a FAISS index from the embeddings and documents.
    5. Saves the FAISS index to a local file.
    """
    print("Starting to build the vector store...")

    # 1. Load documents from the knowledge base directory
    try:
        loader = DirectoryLoader(KNOWLEDGE_BASE_DIR, glob="**/*.md", loader_cls=TextLoader)
        documents = loader.load()
        if not documents:
            print(f"No documents found in '{KNOWLEDGE_BASE_DIR}'. Please add your knowledge files.")
            return
        print(f"Loaded {len(documents)} documents.")
    except Exception as e:
        print(f"Error loading documents: {e}")
        return

    # 2. Split documents into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    docs = text_splitter.split_documents(documents)
    print(f"Split documents into {len(docs)} chunks.")

    # 3. Initialize the embedding model
    print(f"Loading embedding model: '{EMBEDDING_MODEL}'...")
    try:
        embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    except Exception as e:
        print(f"Error loading embedding model. Make sure you have an internet connection. Error: {e}")
        return

    # 4. Create the FAISS vector store from the documents and embeddings
    print("Creating FAISS vector store...")
    try:
        vector_store = FAISS.from_documents(docs, embeddings)
    except Exception as e:
        print(f"Error creating FAISS vector store: {e}")
        return

    # 5. Save the vector store locally
    print(f"Saving vector store to '{VECTOR_STORE_PATH}'...")
    vector_store.save_local(VECTOR_STORE_PATH)
    print("Vector store built and saved successfully!")

if __name__ == "__main__":
    build_vector_store()