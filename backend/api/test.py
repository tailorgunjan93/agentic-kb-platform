from fastapi import APIRouter, Depends, Query
from db.conncet import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from db.quries import fetch_all_chunks
from vectorstore.index import build_faiss_index, get_chunks_fast




router = APIRouter()

@router.get("/health")
async def health_check():
    """Simple health check endpoint"""
    return {"status": "healthy", "message": "API is working!"}

@router.get("/chunks")
async def get_chunks(
    limit: int = Query(default=10, ge=1, le=1000, description="Number of chunks to return"),
    offset: int = Query(default=0, ge=0, description="Offset for pagination")
):
    """Fast endpoint to get chunks with pagination (uses cache)"""
    try:
        # Use cached chunks for fast response
        all_chunks = await get_chunks_fast()
        
        # Apply pagination
        paginated_chunks = all_chunks[offset:offset+limit]
        
        return {
            "success": True,
            "total": len(all_chunks),
            "count": len(paginated_chunks),
            "offset": offset,
            "limit": limit,
            "chunks": paginated_chunks
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {
            "success": False,
            "error": str(e),
            "type": type(e).__name__
        }

@router.get("/test-chunks")
async def test_chunks(rebuild: bool = Query(default=False, description="Force rebuild FAISS index")):
    """Get all chunks and optionally rebuild FAISS index"""
    print('in test chunks')
    try:
        # Use cached version by default, only rebuild if requested
        chunks = await build_faiss_index(use_cache=not rebuild)
        return {
            "success": True,
            "count": len(chunks) if chunks else 0,
            "rebuilt": rebuild,
            "chunks": chunks
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {
            "success": False,
            "error": str(e),
            "type": type(e).__name__
        }