from db.conncetion import get_conncetion,release_connection
from uuid import uuid4
from datetime import datetime
from config import DB_CONFIG
import psycopg2

def insert_file(conn,filename: str, path: str) -> str:
    file_id = str(uuid4())
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO files (id, filename, path, uploaded_at)
            VALUES (%s, %s, %s, %s)
        """, (file_id, filename, path, datetime.now()))
    conn.commit()
    return file_id


def insert_embeddings(conn,file_id: str, chunks: list[str], vectors: list):
    with conn.cursor() as cur:
        for i, (chunk, vector) in enumerate(zip(chunks, vectors)):
            cur.execute("""
                INSERT INTO embeddings (id, file_id, chunk_index, content, embedding, created_at)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                str(uuid4()), file_id, i, chunk, vector.tolist(), datetime.now()
            ))
    conn.commit()
    


def fetch_all_files():
    conn = get_conncetion()
    with conn.cursor() as cur:
        cur.execute("""
            SELECT id, filename, path, uploaded_at
            FROM files
            ORDER BY uploaded_at DESC
        """)
        rows = cur.fetchall()
    release_connection(conn)
    return [
        {"id": str(row[0]), "filename": row[1], "path": row[2], "uploaded_at": row[3].isoformat()}
        for row in rows
    ]
