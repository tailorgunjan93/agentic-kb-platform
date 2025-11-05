from pydantic import BaseModel,Field
from typing import Optional,List

class AgentState(BaseModel):
    agent_id: str = Field(None,description="this is uniquw agent id")
    query: str = Field(None,description="this is user input given in query")
    retrieved_docs:  Optional[List[str]]  = Field(None,description="documents retrieved from data base")
    summary: Optional[str] = Field(None,description="summary for the content")
    intent: Optional[str] = Field(None,description="what should node do this is in intent")
    next:Optional[str]=Field(None,description="next node to route")
