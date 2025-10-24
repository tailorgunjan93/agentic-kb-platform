from fastapi import Query,APIRouter,HTTPException
from typing import List
from db.models import FileListResponse
from utils.embedding_utils import embed_text
from db.async_query import semantic_search
from config import setup_logger
 

logger = setup_logger()
router = APIRouter()

@router.get("/",response_model=FileListResponse)
async def search(query:str=Query(...)):
    try:
        logger.info("in search")
        print("in semantic search")
        vector = embed_text(query)
        result = await semantic_search(vector)
        return FileListResponse(files= result) 
    except Exception as e:
        logger.error(f"semantic search error {e}") 
        raise HTTPException(status_code=500,detail=str(e))

    
    
    

