import re


def split_into_sections(text):
    sections = []

    current_heading = "Document Information"
    current_lines = []

    for line in text.splitlines():

        if line.startswith("# "):

            if current_lines:
                sections.append(
                    (
                        current_heading,
                        "\n".join(current_lines).strip(),
                    )
                )

            current_heading = line.replace(
                "# ",
                "",
                1,
            ).strip()

            current_lines = []

        else:
            current_lines.append(line)

    if current_lines:
        sections.append(
            (
                current_heading,
                "\n".join(current_lines).strip(),
            )
        )

    return sections


def clean_text(text):
    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text,
    )

    return text.strip()


def chunk_documents(documents):
    chunks = []

    chunk_id = 0

    for document in documents:

        sections = split_into_sections(
            document["text"]
        )

        for heading, section_text in sections:

            section_text = clean_text(
                section_text
            )

            if len(section_text) < 30:
                continue

            searchable_text = f"""
Document: {document['document_id']}
Title: {document['title']}
Type: {document['document_type']}
Process: {document['process']}
Product: {document['product']}
Section: {heading}

{section_text}
""".strip()

            chunks.append(
                {
                    "chunk_id": chunk_id,
                    "document_id": document[
                        "document_id"
                    ],
                    "document_type": document[
                        "document_type"
                    ],
                    "title": document["title"],
                    "process": document["process"],
                    "product": document["product"],
                    "section": heading,
                    "path": document["path"],
                    "text": section_text,
                    "searchable_text": searchable_text,
                }
            )

            chunk_id += 1

    return chunks