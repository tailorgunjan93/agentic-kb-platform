from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import List

class FileRecords(BaseModel):
    id : UUID
    filename :str
    path : str
    uploaded_at :datetime

class FileListResponse(BaseModel):
    files:List[FileRecords]

class IngestResponse(BaseModel):
    status:str
    chunks:int

class SearchResult(BaseModel):
    query:str
    results:List[str]
