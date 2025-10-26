from db.async_pool import get_conncetion,release_conncetion
from db.models import FileRecords
from datetime import datetime
from uuid import uuid4
import json

async def semantic_search(query_vector:list[float]):
     conn = await get_conncetion()
     try:
          rows = await conn.fetch("""
            SELECT 
                f.filename,
                e.content AS chunk_text,
                (1 - (e.embedding <=> $1)) AS score
            FROM files f
            JOIN embeddings e ON f.id = e.file_id
            ORDER BY e.embedding <=> $1 ASC
            LIMIT 10
        """, query_vector)

          # Group by filename
          results = {}
          for row in rows:
              filename = row["filename"]
              if filename not in results:
                  results[filename] = []
              results[filename].append({
                  "chunk_text": row["chunk_text"],
                  "score": float(row["score"])
              })
          
          return [
              {"filename": filename, "chunks": chunks}
              for filename, chunks in results.items()
          ]
     except Exception as e:
         raise Exception(e)
     finally:
        await release_conncetion(conn)
                                 

async def fetch_all_files():
    conn = await get_conncetion()
    try:
        
        rows = await conn.fetch("""
            SELECT id, filename, path, uploaded_at
            FROM files
            ORDER BY uploaded_at DESC
        """)
        return [
           FileRecords(
               id=str(row["id"]),
               filename=row["filename"],
               path=row["path"],
               uploaded_at=row["uploaded_at"]
               )
            for row in rows
        ]
    finally:
        await release_conncetion(conn)
    
async def insert_file(conn,filename: str, path: str) -> str:
    file_id = str(uuid4())
    await conn.execute("""
            INSERT INTO files (id, filename, path, uploaded_at)
            VALUES ($1, $2, $3, $4)
        """, file_id, filename, path, datetime.now())
    
    return file_id


async def insert_embeddings(conn,file_id: str, chunks: list[str], vectors: list):
    
        for i, (chunk, vector) in enumerate(zip(chunks, vectors)):
           await conn.execute("""
                INSERT INTO embeddings (id, file_id, chunk_index, content, embedding, created_at)
                VALUES ($1, $2, $3, $4, $5, $6)
            """, 
                str(uuid4()), file_id, i, chunk, vector, datetime.now()
            )        

