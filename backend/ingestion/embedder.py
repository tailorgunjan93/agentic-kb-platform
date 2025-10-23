from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
def generate_dummy_embedding(dim=1536):
    """
    Generates a dummy embedding vector of fixed dimension.

    Args:
        dim (int): Dimension of the embedding (default: 1536).

    Returns:
        List[float]: A list of float values representing the embedding.
    """
    return [0.001] * dim

def embed_chunks(chunks):
    """
    Generates dummy embeddings for a list of text chunks.

    Args:
        chunks (List[str]): List of text chunks.

    Returns:
        List[List[float]]: List of embedding vectors.
    """
    try:
        embeddings = model.encode(chunks,convert_to_numpy=True)
        return embeddings
    except Exception as e:
        raise RuntimeError(f"Huggingface embedding failed {e}")

