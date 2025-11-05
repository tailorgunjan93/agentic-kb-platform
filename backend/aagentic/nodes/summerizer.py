from memory.memory import MemoryManager
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.documents import Document 

from models import AgentState
from dotenv import load_dotenv
import os
load_dotenv()

memory = MemoryManager()

def summarize_node(state:AgentState)->AgentState:
    docs = state.retrieved_docs or  []
    if not docs:
        state.summary = "no document to summarize"
        return state
    documents = [Document(page_content = doc) for doc in docs]
    summary_style = "bullets"
    llm = ChatGoogleGenerativeAI(
        model=os.getenv("MODEL"),
        api_key = os.getenv("GEMINI_API_KEY")
    )
    prompt = (
        "Summarize the following documents in bullet points:\n\n" +
        "\n\n".join([doc.page_content for doc in documents])
    )

    output =llm.invoke(prompt)
    state.summary = output.content.strip()

    print(f"[Summarizer] Generated summary ({summary_style}):\n{state.summary[:200]}...")
    return state




# # Summarizer node: condenses retrieved content into a summary
# def summerize_docs(state:dict)->dict:
#     docs = state.get("docs",[])
#     query = state["input"]
#     context  = "\n\n".join([d.page_content for d in docs])
#     prompt = PromptTemplate.from_template(
#         "Summarize the following content:\n\n{context}\n\nQuery: {query}"
#     )
#     chain = prompt | StrOutputParser()
#     summary = chain.invoke({"context":context,"query":query})
#     return {**state,"output":summary}

# summarize_node = RunnableLambda(summerize_docs)
