from pathlib import Path


def parse_metadata(text):
    metadata = {}

    for line in text.splitlines():
        if line.startswith("#"):
            break

        if ":" in line:
            key, value = line.split(":", 1)

            key = key.strip().lower()
            value = value.strip()

            metadata[key] = value

    return metadata


def load_documents(data_directory):
    data_directory = Path(data_directory)

    documents = []

    for file_path in sorted(data_directory.rglob("*.md")):
        text = file_path.read_text(
            encoding="utf-8"
        )

        metadata = parse_metadata(text)

        documents.append(
            {
                "path": str(file_path),
                "text": text,
                "document_id": metadata.get(
                    "document_id",
                    file_path.stem,
                ),
                "document_type": metadata.get(
                    "document_type",
                    "Unknown",
                ),
                "title": metadata.get(
                    "title",
                    file_path.stem,
                ),
                "process": metadata.get(
                    "process",
                    "Unknown",
                ),
                "product": metadata.get(
                    "product",
                    "Unknown",
                ),
                "status": metadata.get(
                    "status",
                    "Unknown",
                ),
            }
        )

    return documents