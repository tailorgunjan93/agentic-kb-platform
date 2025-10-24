from fastapi import FastAPI
from router.ingestion_router import router as ingestion_router
from router.get_files_router import router as file_router
from router.search_router import router as search_router
from db.async_pool import init_pool,db_pool
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_pool()
    yield 
    if db_pool:
        await db_pool.close()
app = FastAPI(lifespan=lifespan)


app.include_router(ingestion_router,prefix="/ingest",tags=["Ingestion"])
app.include_router(file_router,prefix="/files",tags=["File Registry"])
app.include_router(search_router,prefix="/search",tags=["Semantic search"])
