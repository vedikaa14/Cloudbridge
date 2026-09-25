from pathlib import Path

documents_path = Path("data/documents")

files = [
    "aws_s3.txt",
    "azure_blob.txt",
    "gcp_cloud_storage.txt"
]

documents = []

for file in files:
    file_path = documents_path / file

    text = file_path.read_text(encoding="utf-8")

    document = {
        "page_content": text,
        "metadata": {
            "source": str(file_path)
        }
    }

    documents.append(document)

print(f"Loaded {len(documents)} documents.")

for document in documents:
    print("\n--- DOCUMENT ---")
    print(document["page_content"])
    print("SOURCE:", document["metadata"]["source"])