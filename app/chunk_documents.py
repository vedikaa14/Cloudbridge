from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter


# 1. Location of our documents
documents_path = Path("data/documents")

files = [
    "aws_s3.txt",
    "azure_blob.txt",
    "gcp_cloud_storage.txt"
]


# 2. Create the text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)


# 3. Load and split each document
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


# 4. Display the results
print(f"Total chunks created: {len(all_chunks)}")

for i, chunk in enumerate(all_chunks):
    print(f"\n--- CHUNK {i + 1} ---")
    print(chunk["page_content"])
    print("SOURCE:", chunk["metadata"]["source"])