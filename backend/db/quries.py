from sqlalchemy.future import select
from db.conncet import get_session
from models.chunk import Embeddings 
from sqlalchemy.orm import joinedload


async def fetch_all_chunks(db)->list[dict]:
    """Fetch all text chunks with file metadata from database"""
    print('in fetch all chunks')
    print(f"db :{db}")
    # Query embeddings table with file join
    result = await db.execute(select(Embeddings).options(joinedload(Embeddings.file)))
    print('after select query')      
    # Format results for API consumption
    chunk =  result.scalars().all()
    return [{"chunk_text":c.content,"file_id":c.file_id,"filename":c.file.filename if c.file else "Unknown"} for c in chunk]
