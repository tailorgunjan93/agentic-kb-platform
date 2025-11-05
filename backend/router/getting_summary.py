from fastapi import APIRouter,Query,Request
from models.AgentState import AgentState
from aagentic.langgraph.build_graph import build_graph
import string
import random
from pydantic import BaseModel

class AgenticRequest(BaseModel):
    query: str
    agent_id: str

router = APIRouter()
graph = build_graph()

@router.post("/",response_model=AgentState)
async def summary_router(request:AgenticRequest):
    state = AgentState(**request.dict())
    final_state = await graph.ainvoke(state)
    return final_state