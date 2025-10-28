from langchain_core.runnables import RunnableLambda
# Router node: decides which path to follow based on query intent

def clasify_query(state:dict)->dict:
    query = state["input"].lower()
    # Simple keyword-based routing logic
    if "summarize" in query or "oveview" in query:
        route = "summarize"
    elif "search" in query or "latest" in query or "news" in query:
        route = "internet"
    elif "file" in query or "upload date" in query or "size" in query:
        route = "tool"

    else:
        route = "retrieve"
    # Add route to state
    return {**state,"route":route}

router_node = RunnableLambda(clasify_query)



