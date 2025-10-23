import psycopg2
import uuid
from datetime import datetime

def insert_embeddings(conn, file_id, chunks, vectors):
    """
    Inserts text chunks and their embeddings into the 'embeddings' table.

    Args:
        conn (psycopg2.Connection): Active PostgreSQL connection.
        file_id (UUID): ID of the file these chunks belong to.
        chunks (List[str]): List of text chunks.
        vectors (List[List[float]]): Corresponding embedding vectors.
    """
    cur = conn.cursor()
    for idx, (chunk, vector) in enumerate(zip(chunks, vectors)):
        embedding = vector.tolist()
        cur.execute("""
            INSERT INTO embeddings (id, file_id, chunk_index, content, embedding, created_at)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            str(uuid.uuid4()),  # Unique ID for each embedding row
            file_id,
            idx,
            chunk,
            embedding,
            datetime.now()
        ))
    conn.commit()
    cur.close()