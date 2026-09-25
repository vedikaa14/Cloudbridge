import os
from dotenv import load_dotenv
from google import genai

from app.search import retrieve_context


# Load variables from .env
load_dotenv()


# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def build_context(results):
    """
    Convert retrieved chunks into text
    that can be given to an LLM.
    """

    context = ""

    for result in results:
        context += f"""
[{result['cloud']}]

{result['text']}

Source: {result['source']}

"""

    return context


def generate_answer(question, context):
    """
    Generate an answer using Gemini
    and the retrieved RAG context.
    """

    prompt = f"""
You are CloudBridge, a multi-cloud documentation assistant.

Answer the user's question using ONLY the provided context.

If the context does not contain enough information,
say that the information is not available in the provided documents.

Question:
{question}

Context:
{context}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":

    question = "Compare AWS S3, Azure Blob Storage, and Google Cloud Storage."

    results = retrieve_context(question)

    context = build_context(results)

    answer = generate_answer(question, context)

    print("\n========== FINAL ANSWER ==========")
    print(answer)