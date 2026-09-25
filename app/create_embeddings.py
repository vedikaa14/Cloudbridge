from pathlib import Path
import json
import faiss
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter


# 1. Load documents
documents_path = Path("data/documents")

files = [
    "aws_s3.txt",
    "azure_blob.txt",
    "gcp_cloud_storage.txt"
]


# 2. Create text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)


# 3. Create chunks
all_chunks = []

for file in files:
    file_path = documents_path / file

    text = file_path.read_text(encoding="utf-8")

    chunks = text_splitter.split_text(text)

    for chunk in chunks:
        all_chunks.append({
            "page_content": chunk,
            "metadata": {
                "source": str(file_path)
            }
        })


print("Total chunks:", len(all_chunks))


# 4. Extract text from chunks
texts = [chunk["page_content"] for chunk in all_chunks]


# 5. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 6. Convert chunks into embeddings
embeddings = model.encode(
    texts,
    convert_to_numpy=True
)


print("Embedding shape:", embeddings.shape)


# 7. Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)


print("Vectors stored in FAISS:", index.ntotal)


# 8. Save FAISS index
Path("data").mkdir(exist_ok=True)

faiss.write_index(
    index,
    "data/faiss_index.bin"
)


# 9. Save chunks and metadata
with open(
    "data/chunks.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(
        all_chunks,
        file,
        indent=2
    )


print("FAISS index saved successfully.")
print("Chunk data saved successfully.")
