from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.ingestion_router import router as ingestion_router
from router.get_files_router import router as file_router
from router.search_router import router as search_router
from router.getting_summary import router as summary_router
from db.async_pool import init_pool,db_pool
from contextlib import asynccontextmanager
import asyncio
from vectorstore.index import build_faiss_index
from api.test import router as test_router
from router.faiss_search import router as faiss_search_router
from aagentic.langgraph.build_graph import build_graph
import asyncio


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_pool()
    yield 
    if db_pool:
        await db_pool.close()
app = FastAPI(lifespan=lifespan)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(ingestion_router,prefix="/ingest",tags=["Ingestion"])
app.include_router(file_router,prefix="/files",tags=["File Registry"])
app.include_router(search_router,prefix="/search",tags=["Semantic search"])
app.include_router(test_router,prefix="/api",tags=["Test"])
app.include_router(faiss_search_router,prefix="/faiss",tags=["FAISS search"])
app.include_router(summary_router,prefix="/summary",tags=["summary"])

@app.on_event("startup")
async def startup_event():
    # Build index in background to not block server startup
    asyncio.create_task(build_faiss_index_on_startup())

async def build_faiss_index_on_startup():
    """Build FAISS index on startup without blocking"""
    try:
        print("🚀 Starting FAISS index build in background...")
        chunks = await build_faiss_index(use_cache=False)
        print(f"✅ Startup complete: {len(chunks)} chunks indexed")
    except Exception as e:
        print(f"❌ Error building FAISS index on startup: {e}")
        import traceback
        traceback.print_exc()

