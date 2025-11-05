import pytest
from memory.memory import MemoryManager
from aagentic.nodes.summerizer import summarize_node
from aagentic.nodes.router import router_node
from aagentic.nodes.retrieve import retriever_node

memory = MemoryManager()

@pytest.fixture
def agent_id():
    return "test-agent"

@pytest.fixture
def query():
    return "Summarize LangGraph architecture"

def test_router_node_sets_intent(agent_id, query):
    state = {"agent_id": agent_id, "query": query}
    intent = router_node(state)
    assert intent == "summarize"
    assert memory.get_intent(agent_id) == "summarize"

def test_retriever_node_returns_docs(agent_id):
    state = {"agent_id": agent_id, "query": "What is FAISS?"}
    result = retriever_node(state)
    assert "retrieved_docs" in result
    assert isinstance(result["retrieved_docs"], list)
    assert len(result["retrieved_docs"]) > 0

def test_summarizer_node_creates_summary(agent_id):
    docs = ["LangGraph is a stateful orchestration framework.", "It enables modular agent flows."]
    state = {"agent_id": agent_id, "query": "Summarize LangGraph", "retrieved_docs": docs}
    result = summarize_node(state)
    assert "summary" in result
    assert "LangGraph" in result["summary"]
    assert memory.get_summary(agent_id) == result["summary"]
    assert memory.save_state(agent_id)["summary"] == result["summary"]