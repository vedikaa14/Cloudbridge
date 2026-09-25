import json
import faiss
from sentence_transformers import SentenceTransformer


# Load FAISS index
index = faiss.read_index("data/faiss_index.bin")


# Load chunks and metadata
with open("data/chunks.json", "r", encoding="utf-8") as file:
    chunks = json.load(file)


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve_context(question, top_k=6):
    """
    Retrieve relevant chunks and select
    the best chunk from each cloud.
    """

    # Convert question into an embedding
    question_embedding = model.encode(
        [question],
        convert_to_numpy=True
    )

    # Search FAISS for the top relevant chunks
    distances, indices = index.search(
        question_embedding,
        k=min(top_k, len(chunks))
    )

    # Group results by cloud
    cloud_results = {
        "AWS": [],
        "Azure": [],
        "GCP": []
    }

    for i, index_number in enumerate(indices[0]):

        chunk = chunks[index_number]

        source = chunk["metadata"]["source"].lower()

        if "aws" in source:
            cloud = "AWS"

        elif "azure" in source:
            cloud = "Azure"

        elif "gcp" in source:
            cloud = "GCP"

        else:
            continue

        cloud_results[cloud].append({
            "cloud": cloud,
            "text": chunk["page_content"],
            "source": chunk["metadata"]["source"],
            "distance": float(distances[0][i])
        })

    # Select the best chunk from each cloud
    selected_results = []

    for cloud in ["AWS", "Azure", "GCP"]:

        if cloud_results[cloud]:

            best_result = min(
                cloud_results[cloud],
                key=lambda x: x["distance"]
            )

            selected_results.append(best_result)

    return selected_results


# Test the retrieval function
if __name__ == "__main__":

    question = "Compare AWS S3, Azure Blob Storage, and Google Cloud Storage."

    results = retrieve_context(question)

    print("\nQuestion:")
    print(question)

    print("\n========== RETRIEVED CONTEXT ==========")

    for i, result in enumerate(results):

        print(f"\n--- RESULT {i + 1} ---")
        print("Cloud:", result["cloud"])
        print(result["text"])
        print("Source:", result["source"])
        print("Distance:", result["distance"])