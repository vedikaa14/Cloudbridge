from fastapi import FastAPI
from pydantic import BaseModel

from app.search import retrieve_context
from app.generate_answer import build_context, generate_answer


app = FastAPI(
    title="CloudBridge API",
    description="AI-powered multi-cloud RAG assistant",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "CloudBridge API is running"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    # 1. Retrieve relevant chunks
    results = retrieve_context(request.question)

    # 2. Build context
    context = build_context(results)

    # 3. Generate answer using Gemini
    answer = generate_answer(
        request.question,
        context
    )

    # 4. Return answer and sources
    sources = []

    for result in results:
        sources.append({
            "cloud": result["cloud"],
            "source": result["source"]
        })

    return {
        "question": request.question,
        "answer": answer,
        "sources": sources
    }