from sentence_transformers import SentenceTransformer


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


_model = None


def get_embedding_model():
    global _model

    if _model is None:
        _model = SentenceTransformer(
            MODEL_NAME
        )

    return _model


def embed_texts(texts):
    model = get_embedding_model()

    embeddings = model.encode(
        texts,
        normalize_embeddings=True,
        show_progress_bar=False,
    )

    return embeddings


def embed_query(query):
    model = get_embedding_model()

    embedding = model.encode(
        [query],
        normalize_embeddings=True,
        show_progress_bar=False,
    )

    return embedding