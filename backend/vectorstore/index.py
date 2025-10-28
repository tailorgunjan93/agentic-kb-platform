"""Utility helpers for building and caching the FAISS vector index."""

from utils.embedding_utils import embed_text,embedder
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from db.quries import fetch_all_chunks
from db.conncet import get_session
import asyncio

# Global cache for FAISS index instances and raw chunks so we avoid
# rebuilding or re-fetching data unnecessarily between requests.
_faiss_index_cache = None
_chunks_cache = None

async def build_faiss_index(use_cache=True):
    """Build FAISS index from database chunks. Set use_cache=False to force rebuild."""
    global _faiss_index_cache, _chunks_cache

    # Return cached data if available to avoid redundant DB work.
    if use_cache and _chunks_cache is not None:
        print(f"Using cached index with {len(_chunks_cache)} chunks")
        return _chunks_cache

    print("Building FAISS index from database...")
    db = await anext(get_session())
    chunks = await fetch_all_chunks(db)
    
    if not chunks:
        print("No chunks found in database")
        return chunks
    
    print(f"Processing {len(chunks)} chunks...")
    
    # Create langchain Document objects for each stored chunk so FAISS can
    # associate the embedded vectors with their metadata.
    docs = [Document(
        page_content=c["chunk_text"],
        metadata={"fileid":c["file_id"],"filename":c["filename"]}
    ) for c in chunks]

    # Build FAISS index with progress indication
    print("Creating embeddings and building FAISS index...")
    index = FAISS.from_documents(docs, embedder)

    # Persist the index locally so it can be reloaded without reprocessing.
    try:
        index.save_local("faiss_index")
        print("✅ FAISS index saved successfully.")
    except Exception as e:
        print(f"⚠️ Error saving FAISS index: {e}")

    # Cache the results in memory for subsequent fast access.
    _faiss_index_cache = index
    _chunks_cache = chunks

    print(f"✅ Index built with {len(chunks)} chunks")
    return chunks

async def get_chunks_fast(limit=None):
    """Fast endpoint to get chunks without rebuilding index"""
    global _chunks_cache
    
    if _chunks_cache is None:
        # Cache miss: fetch chunks directly from the database without building the index,
        # keeping the response lightweight for cheap health/debug endpoints.
        db = await anext(get_session())
        chunks = await fetch_all_chunks(db)
        _chunks_cache = chunks
    
    if limit:
        # Optional limit lets API clients request only the first N chunks to reduce payload size.
        return _chunks_cache[:limit]
    # Default behaviour returns the full cached chunk list.
    return _chunks_cache

def load_faiss_index()->FAISS:
    """Load FAISS index from cache or disk"""
    global _faiss_index_cache
    
    if _faiss_index_cache is not None:
        # Reuse the in-memory index if it has already been built in the current process.
        return _faiss_index_cache
    
    # Fall back to loading the index stored on disk (created during build_faiss_index).
    return FAISS.load_local("faiss_index", embeddings=embedder)

def get_cached_index():
    """Get the cached FAISS index"""
    # This helper is used by routes/tests that only need to inspect the cached instance.
    return _faiss_index_cache