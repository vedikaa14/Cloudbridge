
# CloudBridge – AI-Powered Multi-Cloud RAG Assistant

CloudBridge is an AI-powered Retrieval-Augmented Generation (RAG) application that helps users compare cloud services across **AWS, Microsoft Azure, and Google Cloud Platform (GCP)**.

The system retrieves relevant information from cloud service documents using semantic search and uses **Google Gemini** to generate answers based on the retrieved context.

---

## 🚀 Features

- Compare cloud services across AWS, Azure, and GCP
- Document-based question answering using RAG
- Semantic search using vector embeddings
- FAISS-based vector similarity search
- Gemini-powered answer generation
- FastAPI REST API
- Source information included with responses
- Modular document ingestion and retrieval pipeline

---

## 🏗️ System Architecture

```text
                Cloud Documentation
                        │
                        ▼
                Document Loading
                        │
                        ▼
                    Chunking
                        │
                        ▼
                  Embeddings
                        │
                        ▼
                 FAISS Vector Index
                        │
                        │
                        ▼
                  User Question
                        │
                        ▼
               Question Embedding
                        │
                        ▼
                Semantic Retrieval
                        │
                        ▼
                Relevant Context
                        │
                        ▼
                     Gemini
                        │
                        ▼
                  Final Answer


RAG Workflow

CloudBridge follows a Retrieval-Augmented Generation pipeline:

1. Document Loading

Cloud service information is loaded from the data/documents directory.

The current dataset contains information about:

AWS S3
Azure Blob Storage
Google Cloud Storage
2. Document Chunking

Documents are divided into smaller chunks using LangChain's RecursiveCharacterTextSplitter.

This makes the documents easier to process and retrieve efficiently.

3. Embedding Generation

Each document chunk is converted into a numerical vector using the all-MiniLM-L6-v2 Sentence Transformer model.

These vectors represent the semantic meaning of the text.

4. Vector Storage

The generated embeddings are stored in a FAISS vector index.

FAISS is used for efficient vector similarity search.

5. Semantic Retrieval

When a user submits a question:

The question is converted into an embedding.
FAISS searches for semantically similar document chunks.
Relevant context is retrieved from the cloud documentation.
6. Answer Generation

The retrieved context and user question are passed to Google Gemini.

Gemini generates the final answer using the retrieved information.

🛠️ Tech Stack
Technology	Purpose
Python	Core application development
FastAPI	REST API development
LangChain Text Splitters	Document chunking
Sentence Transformers	Text embeddings
FAISS	Vector similarity search
Google Gemini	AI answer generation
Pydantic	API request validation
Git & GitHub	Version control

📂 Project Structure
Cloudbridge/
│
├── app/
│   ├── __init__.py
│   ├── load_documents.py
│   ├── chunk_documents.py
│   ├── create_embeddings.py
│   ├── search.py
│   ├── generate_answer.py
│   └── main.py
│
├── data/
│   ├── documents/
│   │   ├── aws_s3.txt
│   │   ├── azure_blob.txt
│   │   └── gcp_cloud_storage.txt
│   │
│   ├── chunks.json
│   └── faiss_index.bin
│
├── .gitignore
├── requirements.txt
└── README.md
🔌 API Endpoints

CloudBridge provides a REST API using FastAPI.

Health Check
GET /

Response:

{
  "message": "CloudBridge API is running"
}
Ask a Question
POST /ask

Request:

{
  "question": "Compare AWS S3, Azure Blob Storage, and Google Cloud Storage."
}

The API returns:

The user's question
The generated answer
Retrieved document sources

Example response structure:

{
  "question": "Compare AWS S3, Azure Blob Storage, and Google Cloud Storage.",
  "answer": "Generated answer based on the retrieved context.",
  "sources": [
    {
      "cloud": "AWS",
      "source": "data\\documents\\aws_s3.txt"
    },
    {
      "cloud": "Azure",
      "source": "data\\documents\\azure_blob.txt"
    },
    {
      "cloud": "GCP",
      "source": "data\\documents\\gcp_cloud_storage.txt"
    }
  ]
}
▶️ Run Locally
1. Clone the repository
git clone https://github.com/vedikaa14/Cloudbridge.git
cd Cloudbridge
2. Create a virtual environment
python -m venv venv

Activate it on Windows:

.\venv\Scripts\Activate.ps1
3. Install dependencies
pip install -r requirements.txt
4. Configure the Gemini API Key

Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here

Do not commit the .env file to GitHub.

The .env file is already excluded through .gitignore.

5. Start the FastAPI server
uvicorn app.main:app --reload

The API will run at:

http://127.0.0.1:8000
📖 Interactive API Documentation

FastAPI automatically provides interactive API documentation through Swagger UI.

Open:

http://127.0.0.1:8000/docs

From Swagger UI, you can test the /ask endpoint directly.

💡 Example Use Case
Question
Compare AWS S3, Azure Blob Storage, and Google Cloud Storage.
Processing Flow
User Question
      │
      ▼
Question Embedding
      │
      ▼
FAISS Similarity Search
      │
      ▼
Relevant AWS + Azure + GCP Context
      │
      ▼
Google Gemini
      │
      ▼
Grounded Answer + Sources

CloudBridge can therefore be used as a documentation-based assistant for understanding and comparing cloud services.

🔐 Environment Variables

CloudBridge uses the following environment variable:

GEMINI_API_KEY

The API key should be stored in a local .env file.

The .env file is excluded from version control using .gitignore.

📌 Current Scope

The current version of CloudBridge is an MVP using a small documentation dataset and a local FAISS vector index.

Currently supported:

Text-based documents
AWS, Azure, and GCP cloud service information
Semantic retrieval
Gemini-based answer generation
FastAPI REST API
🔮 Future Improvements

The project can be extended with:

PDF and DOCX document ingestion
Larger cloud documentation collections
Persistent vector databases
Metadata-based filtering
Hybrid keyword and semantic search
Retrieval reranking
Improved source citations
Docker containerization
AWS cloud deployment
Automated document ingestion
Scalable document processing
🎯 Learning Outcomes

Through CloudBridge, the project covers practical implementation of:

Retrieval-Augmented Generation (RAG)
Document processing
Text chunking
Vector embeddings
Semantic search
FAISS vector indexing
LLM-based answer generation
REST API development with FastAPI
Environment variable management
Git and GitHub version control                  