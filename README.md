GPT Workflow Assistant 🤖

A full-stack, deployable AI assistant that answers questions based on a custom knowledge base.
This project uses RAG (Retrieval-Augmented Generation), combining the power of large language models with specific, private information.

✨ Features

Full-Stack Application – Python backend with a modern, responsive frontend

Custom Knowledge Base – Add your own documents to make the assistant an expert on any topic

RAG with FAISS – Efficient similarity search for accurate contextual answers

Interactive Chat UI – Built with Tailwind CSS for a clean, responsive interface

Source Citing – Answers include references to source documents

Ready for Deployment – Works seamlessly on platforms like Vercel or Render

🚀 Getting Started
1. Clone the Repository
git clone https://github.com/your-username/gpt-workflow-assistant.git
cd gpt-workflow-assistant

2. Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Set Up API Key

Get a Gemini API Key from Google AI Studio.

Add it as an environment variable:

export GEMINI_API_KEY="your_api_key_here"

5. Build the Knowledge Base

Add .md or .txt files inside the knowledge_base/ folder.

Run the build script:

python build_vector_store.py

6. Run the Application
python app.py


Open http://127.0.0.1:5000 in your browser.

🌐 Deployment (Vercel Example)

Push your code to GitHub

Import repository into Vercel

Configure project:

Build Command:

pip install -r requirements.txt && python build_vector_store.py


Start Command:

gunicorn app:app


Environment Variable:

GEMINI_API_KEY = your API key

Deploy → Vercel provides a live URL 🎉

🛠️ Tech Stack

Backend: Python, Flask, LangChain, FAISS

Frontend: HTML, Tailwind CSS, JavaScript

AI Model: Google Gemini Pro

📖 Example
<img width="1920" height="864" alt="Screenshot (548)" src="https://github.com/user-attachments/assets/348071bf-cdf7-4074-ae55-585dc4863b98" />
📜 License

This project is licensed under the MIT License.
