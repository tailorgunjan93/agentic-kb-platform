from langgraph.graph import StateGraph,START,END
from  aagentic.nodes.router import router_node
from aagentic.nodes.summerizer import summarize_node
from aagentic.nodes.retrieve import retriever_node
from aagentic.nodes.memory_node import memory_node
from models.AgentState import AgentState

def build_graph():
    builder = StateGraph(AgentState)
    builder.add_node("router",router_node)
    builder.add_node("summarizer",summarize_node)
    builder.add_node("retrieve",retriever_node)
    builder.add_node("memory",memory_node)

    builder.set_entry_point("router")
    builder.add_conditional_edges(
        "router",lambda state:state.next
,
        path_map=
        {
            "search": "retrieve",
            "summarize": "summarizer"
        }

    )
    builder.add_edge("retrieve","summarizer")
    builder.add_edge("summarizer", "memory")
   
    builder.set_entry_point("router")
    builder.set_finish_point("memory")
    return builder.compile()