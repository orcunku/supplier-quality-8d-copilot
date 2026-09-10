from collections import defaultdict

import numpy as np

from src.embeddings import embed_query


def search_chunks(
    query,
    index,
    chunks,
    top_k=25,
):
    query_embedding = embed_query(
        query
    )

    query_embedding = np.asarray(
        query_embedding,
        dtype="float32",
    )

    scores, indexes = index.search(
        query_embedding,
        top_k,
    )

    results = []

    for score, chunk_index in zip(
        scores[0],
        indexes[0],
    ):

        if chunk_index == -1:
            continue

        chunk = chunks[
            int(chunk_index)
        ].copy()

        chunk["similarity"] = float(
            score
        )

        results.append(
            chunk
        )

    return results


def group_by_document(
    chunk_results,
    max_documents=5,
):
    grouped = defaultdict(list)

    for result in chunk_results:
        grouped[
            result["document_id"]
        ].append(result)

    documents = []

    for document_id, matches in grouped.items():

        matches = sorted(
            matches,
            key=lambda item: item[
                "similarity"
            ],
            reverse=True,
        )

        top_match = matches[0]

        top_scores = [
            item["similarity"]
            for item in matches[:3]
        ]

        document_score = (
            sum(top_scores)
            / len(top_scores)
        )

        documents.append(
            {
                "document_id": document_id,
                "document_type": top_match[
                    "document_type"
                ],
                "title": top_match["title"],
                "process": top_match[
                    "process"
                ],
                "product": top_match[
                    "product"
                ],
                "score": document_score,
                "matches": matches[:4],
            }
        )

    documents.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    return documents[
        :max_documents
    ]


def similarity_percentage(score):
    minimum = 0.20
    maximum = 0.85

    normalized = (
        score - minimum
    ) / (
        maximum - minimum
    )

    normalized = max(
        0,
        min(1, normalized),
    )

    return round(
        normalized * 100
    )


def search_documents(
    query,
    index,
    chunks,
    top_k_chunks=30,
    max_documents=5,
):
    chunk_results = search_chunks(
        query=query,
        index=index,
        chunks=chunks,
        top_k=top_k_chunks,
    )

    documents = group_by_document(
        chunk_results,
        max_documents=max_documents,
    )

    for document in documents:
        document[
            "display_score"
        ] = similarity_percentage(
            document["score"]
        )

    return documents