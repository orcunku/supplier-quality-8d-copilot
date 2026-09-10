from pathlib import Path
import sys


BASE_DIR = Path(
    __file__
).resolve().parent.parent

sys.path.insert(
    0,
    str(BASE_DIR),
)


from src.document_loader import load_documents
from src.chunker import chunk_documents
from src.embeddings import embed_texts
from src.vector_store import (
    create_index,
    save_index,
)


DATA_DIR = BASE_DIR / "data"

INDEX_PATH = (
    BASE_DIR
    / "vector_db"
    / "quality.index"
)

METADATA_PATH = (
    BASE_DIR
    / "vector_db"
    / "metadata.json"
)


def main():
    print("Loading documents...")

    documents = load_documents(
        DATA_DIR
    )

    print(
        f"Loaded {len(documents)} documents."
    )

    print("Creating chunks...")

    chunks = chunk_documents(
        documents
    )

    print(
        f"Created {len(chunks)} chunks."
    )

    print(
        "Creating embeddings..."
    )

    texts = [
        chunk["searchable_text"]
        for chunk in chunks
    ]

    embeddings = embed_texts(
        texts
    )

    print(
        "Building FAISS index..."
    )

    index = create_index(
        embeddings
    )

    save_index(
        index=index,
        chunks=chunks,
        index_path=INDEX_PATH,
        metadata_path=METADATA_PATH,
    )

    print()
    print("Success!")
    print(
        f"Vectors stored: {index.ntotal}"
    )
    print(
        f"Index: {INDEX_PATH}"
    )
    print(
        f"Metadata: {METADATA_PATH}"
    )


if __name__ == "__main__":
    main()