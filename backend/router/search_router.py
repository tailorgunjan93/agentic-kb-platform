from fastapi import Query, APIRouter, HTTPException
from typing import List
from db.models import SemanticSearchResult
from utils.embedding_utils import embed_text
from db.async_query import semantic_search
from config import setup_logger

# API router for semantic search functionality
logger = setup_logger()
router = APIRouter()

@router.get("/", response_model=List[SemanticSearchResult])
async def search(query: str = Query(...)):
    """
    Perform semantic search using query embedding.

    This endpoint takes a query string as input, generates an embedding vector for the query text,
    and executes a vector similarity search against the database.

    Args:
        query (str): The search query.

    Returns:
        List[SemanticSearchResult]: A list of search results.

    Raises:
        HTTPException: If an error occurs during the search process.
    """
    try:
        logger.info("in search")
        # Generate embedding vector for the query text
        # This step converts the query string into a numerical representation
        # that can be used for similarity search.
        vector = embed_text(query)
        # Execute vector similarity search against database
        # This step uses the generated vector to search for similar documents
        # in the database and returns a list of search results.
        result = await semantic_search(vector)
        return result 
    except Exception as e:
        # Log any errors that occur during the search process
        logger.error(f"semantic search error {e}") 
        # Raise an HTTP exception with a 500 status code and the error message
        raise HTTPException(status_code=500, detail=str(e))
