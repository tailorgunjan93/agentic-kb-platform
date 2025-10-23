from fastapi import Query,APIRouter
from ingestion.ingest_file import ingest_file
from db.models import IngestResponse
router = APIRouter()

@router.post("/file")
def ingest(file_name : str=Query(...),file_path:str=Query(...)):
    """
    Trigger ingestion for a given file.
    """
    try:
        chunks=ingest_file(file_name,file_path)
        print(chunks)
        return {"status":"success","message":f"{file_name}"}
    except Exception as e:
        return {"status":"error","message":f"{str(e)}"}

