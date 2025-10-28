from db.async_pool import get_conncetion,release_conncetion
from ingestion.chunker import chunk_files
from ingestion.embedder import embed_chunks
from config import DB_CONFIG,setup_logger
from ingestion.utils import resolve_path,insert_embeddings,insert_file_record


logger = setup_logger()



async def ingest_file(file_name,file_path):
    """Ingest a file by chunking, embedding, and storing in the database"""
    # Acquire database connection
    conn = await get_conncetion()
    # Resolve full file path
    full_path = resolve_path(file_path,file_name)
    # Split file into text chunks
    chunks = chunk_files(full_path)
    # Generate embeddings for each chunk
    vector = embed_chunks(chunks)
    logger.info(f"Ingested {len(chunks)} chunks from file {file_name} ")
    # Store file metadata and embeddings
    file_id = await insert_file_record(conn,file_name,file_path)
    await insert_embeddings(conn,file_id,chunks,vector)
    # Release connection
    await release_conncetion(conn)
    return chunks
