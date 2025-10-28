from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Summarizer node: condenses retrieved content into a summary
def summerize_docs(state:dict)->dict:
    docs = state.get("docs",[])
    query = state["input"]
    context  = "\n\n".join([d.page_content for d in docs])
    prompt = PromptTemplate.from_template(
        "Summarize the following content:\n\n{context}\n\nQuery: {query}"
    )
    chain = prompt | StrOutputParser()
    summary = chain.invoke({"context":context,"query":query})
    return {**state,"output":summary}

summarize_node = RunnableLambda(summerize_docs)
