import json
from pathlib import Path

import faiss
import numpy as np


def create_index(embeddings):
    embeddings = np.asarray(
        embeddings,
        dtype="float32",
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(
        dimension
    )

    index.add(
        embeddings
    )

    return index


def save_index(
    index,
    chunks,
    index_path,
    metadata_path,
):
    index_path = Path(index_path)
    metadata_path = Path(metadata_path)

    index_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    faiss.write_index(
        index,
        str(index_path),
    )

    with metadata_path.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            chunks,
            file,
            ensure_ascii=False,
            indent=2,
        )


def load_index(
    index_path,
    metadata_path,
):
    index = faiss.read_index(
        str(index_path)
    )

    with open(
        metadata_path,
        "r",
        encoding="utf-8",
    ) as file:
        chunks = json.load(file)

    return index, chunks