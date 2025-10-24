from db.async_pool import get_conncetion,release_conncetion
from ingestion.chunker import chunk_files
from ingestion.embedder import embed_chunks
from config import DB_CONFIG,setup_logger
from ingestion.utils import resolve_path,insert_embeddings,insert_file_record


logger = setup_logger()



async def ingest_file(file_name,file_path):  
    conn = await get_conncetion()
    full_path = resolve_path(file_path,file_name)
    chunks = chunk_files(full_path)
    vector = embed_chunks(chunks)
    logger.info(f"Ingested {chunks} from file {file_name} ")
    file_id = await insert_file_record(conn,file_name,file_path)
    await insert_embeddings(conn,file_id,chunks,vector)
    await release_conncetion(conn)
    return chunks
    


