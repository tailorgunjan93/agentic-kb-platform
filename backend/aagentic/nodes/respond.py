from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Responder node: generates final answer using LLM
def generate_response(state: dict) -> dict:
    docs = state.get("docs", [])
    query = state["input"]
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = PromptTemplate.from_template(
        "Answer the question based on the context below:\n\n{context}\n\nQuestion: {query}"
    )
    chain = prompt | StrOutputParser()
    response = chain.invoke({"context": context, "query": query})

    return {**state, "output": response}

respond_node = RunnableLambda(generate_response)