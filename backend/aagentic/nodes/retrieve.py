from langchain_core.runnables import RunnableLambda
from langchain_community.vectorstores import FAISS
from utils.embedding_utils import embed_text,embedder
from memory.memory import MemoryManager
from models import AgentState



# Router node: decides which path to follow based on query intent

# Load FAISS index once
index = FAISS.load_local("faiss_index", embedder, allow_dangerous_deserialization=True)

def retriever_node(state:AgentState)->AgentState:
    state_dict = dict(state)
    query = state_dict.get("query")
    query_embedding = embed_text(query)
    docs = index.similarity_search_with_score_by_vector(query_embedding)
    threshold = 0.7
    document = [r.page_content for r,score in docs if score>threshold]
    state.retrieved_docs = document
    print(f"[Retriever] Retrieved {len(docs)} docs above score {threshold}")
    return state



# # Retriever node: fetches relevant chunks from FAISS
# def retrieve_docs(state:dict)->dict:
#     query = state["input"]
#     docs = index.similarity_search(query,embedder)
#     return {**state,"docs":docs}

# retriever_node = RunnableLambda(retrieve_docs)

