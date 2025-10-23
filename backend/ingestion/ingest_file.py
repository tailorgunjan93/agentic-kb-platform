import psycopg2
from chunker import chunk_files
from embedder import embed_chunks
from db_writer import insert_embeddings
from utils import DB_CONFIG,setup_logger
import os

logger = setup_logger()



def ingest_file(file_name,file_path):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT id FROM files WHERE filename = %s", ('human-nutrition-text.pdf',))
    result = cur.fetchone()
    if not result:
        raise ValueError(f"No file found in DB {file_name}")
    file_id = result[0]
    full_path = os.path.join(file_path,file_name)
    chunks = chunk_files(full_path)
    vector = embed_chunks(chunks)
    logger.info(f"Ingested {chunks} from file {file_name} ")
    insert_embeddings(conn,file_id,chunks,vector)
    conn.commit()
    conn.close()
    


