# app.py

import os
from flask import Flask, render_template, request, jsonify
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

# --- Flask App Initialization ---
app = Flask(__name__)

# --- LangChain Initialization ---
qa_chain = None

def initialize_qa_chain():
    """
    Initializes the QA chain. This function is called once when the server starts.
    """
    global qa_chain
    
    print("Initializing QA chain...")

    # Configuration
    VECTOR_STORE_PATH = "vector_store.faiss"
    EMBEDDING_MODEL = "all-MiniLM-L6-v2"

    # 1. Load the Language Model (Gemini)
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set. Please set it before running the app.")
    llm = ChatGoogleGenerativeAI(model="gemini-1.0-pro", google_api_key=api_key)

    # 2. Load the Embedding Model
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    # 3. Load the FAISS Vector Store
    if not os.path.exists(VECTOR_STORE_PATH):
        raise FileNotFoundError(f"Vector store not found at {VECTOR_STORE_PATH}. Please run build_vector_store.py first.")
    vector_store = FAISS.load_local(VECTOR_STORE_PATH, embeddings, allow_dangerous_deserialization=True)

    # 4. Define the Prompt Template (Prompt Tuning)
    prompt_template = """
    You are a helpful workflow assistant. Use the following pieces of context to answer the user's question.
    If you don't know the answer from the context provided, just say that you don't know. Don't try to make up an answer.

    Context:
    {context}

    Question:
    {question}

    Helpful Answer:
    """
    QA_PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    # 5. Create the RetrievalQA Chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(),
        return_source_documents=True,
        chain_type_kwargs={"prompt": QA_PROMPT}
    )
    print("QA chain initialized successfully.")

# --- Flask Routes ---

@app.route('/')
def index():
    """Render the main chat page."""
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    """Handle the POST request for asking a question."""
    if not qa_chain:
        return jsonify({"error": "QA chain is not initialized."}), 500

    data = request.get_json()
    query = data.get("query")

    if not query:
        return jsonify({"error": "Query not provided."}), 400

    try:
        result = qa_chain({"query": query})
        
        # Extract source documents for citation
        source_docs = []
        if result.get("source_documents"):
            source_docs = list(set([doc.metadata.get("source", "unknown") for doc in result["source_documents"]]))

        response_data = {
            "answer": result.get("result"),
            "sources": source_docs
        }
        return jsonify(response_data)

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "An internal error occurred."}), 500

if __name__ == '__main__':
    initialize_qa_chain()
    app.run(debug=True)