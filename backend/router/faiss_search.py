from fastapi import APIRouter, Query, HTTPException
from vectorstore.index import load_faiss_index, build_faiss_index

router = APIRouter()

@router.get("/faiss_search")
async def faiss_search(query: str = Query(..., description="Query string")):
    try:
        # Ensure index is available (will read from cache or rebuild if missing)
        try:
            index = load_faiss_index()
        except Exception:
            # If loading fails (e.g., first run), rebuild synchronously
            await build_faiss_index(use_cache=False)
            index = load_faiss_index()

        results = index.similarity_search_with_score(query, k=5)

        return [
            {
                "text": doc.page_content,
                "score": float(score),
                "file_id": doc.metadata.get("fileid"),
                "filename": doc.metadata.get("filename"),
            }
            for doc, score in results
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))