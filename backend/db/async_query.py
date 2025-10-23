from db.async_pool import get_conncetion,release_conncetion
from db.models import FileRecords

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

