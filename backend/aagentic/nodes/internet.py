from langchain_core.runnables import RunnableLambda
from langchain_community.tools.tavily_search import TavilySearchResults

search_tool = TavilySearchResults()

# Internet node: performs real-time web search
def surf_web(state: dict) -> dict:
    query = state["input"]
    results = search_tool.invoke({"query": query})
    return {**state, "web_results": results}

internet_node = RunnableLambda(surf_web)