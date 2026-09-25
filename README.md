# CloudBridge – AI-Powered Multi-Cloud RAG Assistant

CloudBridge is an AI-powered Retrieval-Augmented Generation (RAG) application...



## 🚀 Features

- Compare cloud services across AWS, Azure, and GCP
- Document-based question answering
- Semantic search
- FAISS vector similarity search



## 🏗️ System Architecture

```text
Cloud Documentation
        ↓
Document Loading
        ↓
Chunking
        ↓
Embeddings
        ↓
FAISS Vector Index
        ↓
Semantic Retrieval
        ↓
Relevant Context
        ↓
Google Gemini
        ↓
Final Answer



🛠️ Tech Stack
Technology	Purpose
Python	Core application
FastAPI	REST API
Sentence Transformers	Embeddings
FAISS	Vector search
Google Gemini	Answer generation
📂 Project Structure
Cloudbridge/
├── app/
├── data/
├── .gitignore
├── requirements.txt
└── README.md
🔄 RAG Workflow
1. Document Loading

Cloud documentation is loaded from the data/documents directory.

2. Document Chunking

Documents are divided into smaller chunks...

3. Embedding Generation

Each chunk is converted into a numerical vector...

4. Vector Storage

The embeddings are stored in FAISS...

5. Semantic Retrieval

The user's question is converted into an embedding and compared with stored vectors.

6. Answer Generation

The retrieved context is passed to Google Gemini...

🔌 API Endpoints
GET /

Health-check endpoint.

POST /ask

Accepts a user question and returns the generated answer and retrieved sources.

▶️ Run Locally
1. Clone the Repository
git clone https://github.com/vedikaa14/Cloudbridge.git
cd Cloudbridge
2. Create Virtual Environment
python -m venv venv
3. Activate Virtual Environment
.\venv\Scripts\Activate.ps1
4. Install Dependencies
pip install -r requirements.txt
5. Configure Gemini API Key

Create .env:

GEMINI_API_KEY=your_api_key_here
6. Start the Application
uvicorn app.main:app --reload
📖 API Documentation

Once the application is running, open:

http://127.0.0.1:8000/docs

This opens the interactive FastAPI Swagger documentation.

💡 Example
Question
Compare AWS S3, Azure Blob Storage, and Google Cloud Storage.
Processing Flow
User Question
      ↓
Question Embedding
      ↓
FAISS Similarity Search
      ↓
Relevant Cloud Context
      ↓
Google Gemini
      ↓
Grounded Answer
🔐 Environment Variables

CloudBridge uses:

GEMINI_API_KEY

The .env file is excluded from Git using .gitignore.

📌 Current Scope

The current version is an MVP using a small documentation dataset and a local FAISS vector index.

Currently supported:

Text-based documents
AWS, Azure, and GCP information
Semantic retrieval
Gemini answer generation
FastAPI REST API
🔮 Future Improvements
PDF and DOCX document ingestion
Larger documentation collections
Persistent vector databases
Metadata filtering
Hybrid search
Retrieval reranking
Improved source citations
Docker containerization
AWS deployment
Automated document ingestion
🎯 Learning Outcomes
Retrieval-Augmented Generation (RAG)
Document processing
Text chunking
Vector embeddings
Semantic search
FAISS
LLM integration
FastAPI REST APIs
Git and GitHub