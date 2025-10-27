from sentence_transformers import SentenceTransformer
from langchain_community.embeddings import HuggingFaceEmbeddings

embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
model = SentenceTransformer("all-MiniLM-L6-v2")
def embed_text(text:str)->list[float]:
    return model.encode(text,normalize_embeddings=True).tolist()