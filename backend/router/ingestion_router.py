from fastapi import Query,APIRouter
from ingestion.ingest_file import ingest_file
from db.models import IngestResponse
from config import setup_logger
logger  = setup_logger()
router = APIRouter()

@router.post("/file")
async def ingest(file_name : str=Query(...),file_path:str=Query(...)):
    """
    Trigger ingestion for a given file.
    """
    try:
        logger.info(f"Getting in api ingets")
        print("comming in api")
        chunks= await ingest_file(file_name,file_path)
        print(chunks)
        return {"status":"success","message":f"{file_name}"}
    except Exception as e:
        return {"status":"error","message":f"{str(e)}"}

