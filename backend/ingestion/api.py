from fastapi import FastAPI,Query
from ingest_file import ingest_file

app = FastAPI()

@app.post("/ingest")
def ingest(file_name : str=Query(...),file_path:str=Query(...)):
    """
    Trigger ingestion for a given file.
    """
    try:
        ingest_file(file_name,file_path)
        return {"status":"success","message":f"{file_name}"}
    except Exception as e:
        return {"status":"error","message":f"{str(e)}"}

