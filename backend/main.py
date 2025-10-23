from fastapi import FastAPI
from ingestion.api import router as ingestion_router
from registry.file_registry import router as file_router
from db.async_pool import init_pool
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_pool()
    yield 
app = FastAPI(lifespan=lifespan)


app.include_router(ingestion_router,prefix="/ingest",tags=["Ingestion"])
app.include_router(file_router,prefix="/files",tags=["File Registry"])
