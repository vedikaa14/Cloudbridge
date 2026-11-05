# CloudBridge – AI-Powered Multi-Cloud RAG Assistant

CloudBridge is an AI-powered Retrieval-Augmented Generation (RAG) application that helps users retrieve and compare cloud-service information across **AWS, Microsoft Azure, and Google Cloud Platform (GCP)**.

The application uses document processing, text chunking, vector embeddings, FAISS-based semantic search, and Google Gemini to generate context-aware answers from the available cloud documentation.

## 🚀 Live Demo

- **Live Application:** https://cloudbridge-42jt.onrender.com
- **API Documentation (Swagger):** https://cloudbridge-42jt.onrender.com/docs

## ✨ Features

- Compare cloud storage services across AWS, Azure, and GCP.
- Document-based question answering.
- Semantic search using vector embeddings.
- FAISS-based vector similarity search.
- Context-aware answer generation using Google Gemini.
- REST API built with FastAPI.
- Interactive API testing through Swagger UI.
- Docker-based application deployment.

## 📌 Current Knowledge Base Scope

**The current version focuses specifically on cloud storage services.**

The knowledge base currently contains information about:

- **AWS:** Amazon Simple Storage Service (Amazon S3)
- **Azure:** Azure Blob Storage
- **GCP:** Google Cloud Storage

CloudBridge retrieves relevant information from these documents to answer questions and compare the supported storage services.

**Note:** Other cloud service categories, such as compute, networking, and databases, are not currently included in the knowledge base. Additional services can be incorporated in future versions.

## 💡 Try These Demo Questions

New users can try the following questions through the live API to explore CloudBridge:

1. What is object storage, and how does it work?
2. What is Amazon S3, and what are its main features?
3. Explain Azure Blob Storage and its use cases.
4. What is Google Cloud Storage used for?
5. Compare Amazon S3, Azure Blob Storage, and Google Cloud Storage.
6. What are the key differences between these three cloud storage services?
7. Which cloud storage service is suitable for storing large amounts of unstructured data?
8. What are the common use cases of cloud object storage?

**How to test:**
1. Open the [Swagger API Documentation](https://cloudbridge-42jt.onrender.com/docs).
2. Expand the `POST /ask` endpoint.
3. Click **Try it out**.
4. Enter a question in the request body.
5. Click **Execute** to view the generated answer and retrieved sources.

## 🏗️ System Architecture

```text
Cloud Documentation
        ↓
Document Loading
        ↓
Text Chunking
        ↓
Gemini Embeddings
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
```

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application |
| FastAPI | REST API development |
| Google Gemini | Answer generation |
| Gemini Embeddings | Text and query embeddings |
| FAISS | Vector similarity search |
| Docker | Application containerization |
| Render | Application hosting |
| Swagger UI | API documentation and testing |

## 📂 Project Structure

```text
Cloudbridge/
│
├── app/
│   ├── main.py
│   ├── create_embeddings.py
│   └── search.py
│
├── data/
│   ├── documents/
│   │   ├── aws_s3.txt
│   │   ├── azure_blob.txt
│   │   └── gcp_cloud_storage.txt
│   ├── chunks.json
│   └── faiss_index.bin
│
├── .gitignore
├── requirements.txt
├── Dockerfile
├── compose.yaml
└── README.md
```

## 🔄 RAG Workflow

### 1. Document Loading
Cloud storage documentation is loaded from the `data/documents` directory.

### 2. Document Chunking
Documents are divided into smaller text chunks to make relevant information easier to retrieve.

### 3. Embedding Generation
Each text chunk is converted into a numerical vector using Gemini Embeddings.

### 4. Vector Storage
The generated embeddings are stored in a FAISS vector index for efficient similarity search.

### 5. Semantic Retrieval
The user's question is converted into an embedding and compared with stored vectors to retrieve relevant document chunks.

### 6. Answer Generation
The retrieved context is passed to Google Gemini to generate a relevant, context-aware answer.

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health-check endpoint |
| POST | `/ask` | Accepts a user question and returns the generated answer and retrieved sources |

## ▶️ Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/vedikaa14/Cloudbridge.git
cd Cloudbridge
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Gemini API Key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

### 6. Start the Application

```bash
uvicorn app.main:app --reload
```

### 7. Open API Documentation

Once the application is running, visit:

http://127.0.0.1:8000/docs

This opens the interactive FastAPI Swagger documentation, where you can test the available API endpoints.

## 🔐 Environment Variables

CloudBridge uses the following environment variable:

- `GEMINI_API_KEY` – API key used to access Google Gemini services.

The `.env` file is excluded from Git using `.gitignore` to prevent exposing sensitive credentials.

## 🔮 Future Improvements

- PDF and DOCX document ingestion.
- Expand the knowledge base with additional AWS, Azure, and GCP services.
- Larger cloud documentation collections.
- Persistent vector database integration.
- Metadata filtering.
- Hybrid search.
- Retrieval reranking.
- Improved source citations.
- Automated document ingestion.

## 🎯 Learning Outcomes

- Retrieval-Augmented Generation (RAG).
- Document processing and text chunking.
- Vector embeddings.
- Semantic search and FAISS.
- Large Language Model (LLM) integration.
- FastAPI REST API development.
- Docker containerization.
- Cloud application deployment.
- Git and GitHub.

---

**CloudBridge** demonstrates how RAG, semantic search, and generative AI can be combined to make multi-cloud storage information easier to retrieve, compare, and understand.