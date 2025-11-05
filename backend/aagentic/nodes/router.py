from langchain_core.runnables import RunnableLambda
from memory.memory import MemoryManager
from models import AgentState
# Router node: decides which path to follow based on query intent
memory = MemoryManager()

def router_node(state:AgentState)->AgentState:
        state_dict = dict(state)
        agent_id = state_dict.get("agent_id","default")
        query = state_dict.get("query","")
        memory.save_query(agent_id,query)
        if "summarize" in query.lower():
             intent = "summarize"
        else:
             intent = "search"
        memory.set_intent(agent_id,intent)
        state.next = intent
        state.intent = intent
        return  state


# def clasify_query(state:dict)->dict:
#     query = state["input"].lower()
#     # Simple keyword-based routing logic
#     if "summarize" in query or "oveview" in query:
#         route = "summarize"
#     elif "search" in query or "latest" in query or "news" in query:
#         route = "internet"
#     elif "file" in query or "upload date" in query or "size" in query:
#         route = "tool"

#     else:
#         route = "retrieve"
#     # Add route to state
#     return {**state,"route":route}

#router_node = RunnableLambda(clasify_query)



