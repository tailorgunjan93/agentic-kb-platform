from utils.embedding_utils import embed_text,embedder
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from db.quries import fetch_all_chunks
from db.conncet import get_session
import asyncio

# Global cache for FAISS index
_faiss_index_cache = None
_chunks_cache = None

async def build_faiss_index(use_cache=True):
    """Build FAISS index from database chunks. Set use_cache=False to force rebuild."""
    global _faiss_index_cache, _chunks_cache
    
    # Return cached data if available
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
    
    # Create documents
    docs = [Document(
        page_content=c["chunk_text"],
        metadata={"fileid":c["file_id"],"filename":c["filename"]}
    ) for c in chunks]
    
    # Build FAISS index with progress indication
    print("Creating embeddings and building FAISS index...")
    index = FAISS.from_documents(docs, embedder)
    
    # Save to disk
    try:
        index.save_local("faiss_index")
        print("✅ FAISS index saved successfully.")
    except Exception as e:
        print(f"⚠️ Error saving FAISS index: {e}")
    
    # Cache the results
    _faiss_index_cache = index
    _chunks_cache = chunks
    
    print(f"✅ Index built with {len(chunks)} chunks")
    return chunks

async def get_chunks_fast(limit=None):
    """Fast endpoint to get chunks without rebuilding index"""
    global _chunks_cache
    
    if _chunks_cache is None:
        # If cache is empty, fetch from DB without building index
        db = await anext(get_session())
        chunks = await fetch_all_chunks(db)
        _chunks_cache = chunks
    
    if limit:
        return _chunks_cache[:limit]
    return _chunks_cache

def load_faiss_index()->FAISS:
    """Load FAISS index from cache or disk"""
    global _faiss_index_cache
    
    if _faiss_index_cache is not None:
        return _faiss_index_cache
    
    return FAISS.load_local("faiss_index", embeddings=embedder)

def get_cached_index():
    """Get the cached FAISS index"""
    return _faiss_index_cache