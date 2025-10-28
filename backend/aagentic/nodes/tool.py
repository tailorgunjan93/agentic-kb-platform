from langchain_core.runnables import RunnableLambda

# Tool node: calls DB or external APIs based on query
def call_tool(state: dict) -> dict:
    query = state["input"]

    # Simulated tool logic (replace with actual DB/API calls)
    if "upload date" in query:
        result = "File was uploaded on 2025-10-01"
    elif "file size" in query:
        result = "File size is 2.3 MB"
    else:
        result = "Tool not matched"

    return {**state, "tool_result": result}

tool_node = RunnableLambda(call_tool)