from langchain_core.runnables import RunnableLambda
from langchain_community.vectorstores import FAISS
from utils.embedding_utils import embed_text,embedder
# Router node: decides which path to follow based on query intent

# Load FAISS index once
index = FAISS.load_local("faiss_index", embedder, allow_dangerous_deserialization=True)

# Retriever node: fetches relevant chunks from FAISS
def retrieve_docs(state:dict)->dict:
    query = state["input"]
    docs = index.similarity_search(query,embedder)
    return {**state,"docs":docs}

retriever_node = RunnableLambda(retrieve_docs)

