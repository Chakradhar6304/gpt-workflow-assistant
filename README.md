GPT Workflow Assistant 🤖
A full-stack, deployable AI assistant that answers questions based on a custom knowledge base. This project uses a RAG (Retrieval-Augmented Generation) architecture, combining the power of large language models with specific, private information.

🚀 View Live Demo

✨ Features
Full-Stack Application: A complete solution with a Python backend and a sleek, modern frontend.

Custom Knowledge Base: Easily add your own documents to create an expert on any topic.

Retrieval-Augmented Generation (RAG): Uses FAISS for efficient similarity search to provide contextually accurate answers.

Interactive Chat Interface: A clean and responsive chat UI built with Tailwind CSS.

Source Citing: The assistant cites the source documents it used to generate an answer.

Ready for Deployment: Can be easily deployed to any platform that supports Python, such as Vercel or Render.

🚀 How to Use
Local Setup
Clone the repository and navigate into it.

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Get a Gemini API Key from Google AI Studio.

Build the Knowledge Base:

Add your .md or .txt files to the knowledge_base/ directory.

Run the build script: python build_vector_store.py

Run the Application:

Set your API key as an environment variable.

Start the Flask server: python app.py

Open http://127.0.0.1:5000 in your browser.

Deployment
This application is ready to be deployed on platforms like Vercel.

Push your code to a GitHub repository.

Import the repository into your Vercel dashboard.

Configure the project:

Build Command: pip install -r requirements.txt && python build_vector_store.py

Start Command: gunicorn app:app

Add Environment Variables: Set GEMINI_API_KEY to your key.

Deploy! Vercel will provide you with a live URL.

🛠️ Tech Stack
Backend: Python, Flask, LangChain, FAISS

Frontend: HTML, Tailwind CSS, JavaScript

AI Model: Google Gemini Pro
