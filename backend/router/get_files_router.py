from fastapi import APIRouter
from db.async_query import fetch_all_files
from db.models import FileListResponse

router = APIRouter()

@router.get("/",response_model=FileListResponse)
async def list_files():
    result =  await fetch_all_files()
    print(result)
    return FileListResponse(files=result)