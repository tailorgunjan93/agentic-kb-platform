from utils.embedding_utils import embed_text
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

def build_faiss_index(chunks:list[dict])->FAISS:
    docs = [Document(page_content=c["chunk_text"],metadata={"filename":c["filename"]})  for c in chunks]
    text = [doc.page_content for doc in docs]
    embeddings = embed_text(text)
    index = FAISS.from_embeddings(embeddings,docs)
    index.save_local("faiss_index")
    return index

def load_faiss_index()->FAISS:
    return FAISS.load_local("faiss_index",embeddings=None)