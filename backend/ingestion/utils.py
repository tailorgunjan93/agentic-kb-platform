import os
from db.async_query import insert_file
import db.query
from config import setup_logger
logger = setup_logger()

def resolve_path(file_path: str, file_name: str) -> str:
    """Normalize and validate full file path."""
    full_path = os.path.abspath(os.path.join(file_path, file_name))
    if not os.path.isfile(full_path):
        raise FileNotFoundError(f"File not found: {full_path}")
    return full_path

async def insert_file_record(conn,filename: str, path: str) -> str:
    """Insert a new file record and return its UUID."""
    file_id =await insert_file(conn,filename,path)
    return file_id

async def insert_embeddings(conn,file_id: str, chunks: list[str], vectors: list):
    """Insert chunked content and embeddings into DB."""
    logger.info("in utils file")
    await db.async_query.insert_embeddings(conn,file_id,chunks,vectors)