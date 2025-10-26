import asyncio
import os
from pathlib import Path
from ingestion.ingest_file import ingest_file

async def ingest_all_files():
    """Ingest all files from the uploads directory"""
    uploads_dir = Path("uploads")
    
    if not uploads_dir.exists():
        print("Uploads directory not found!")
        return
    
    files = [f for f in uploads_dir.iterdir() if f.is_file()]
    
    print(f"Found {len(files)} files to ingest")
    
    for file_path in files:
        file_name = file_path.name
        file_path_str = str(file_path.parent)
        
        print(f"\nIngesting: {file_name}")
        try:
            chunks = await ingest_file(file_name, file_path_str)
            print(f"✓ Successfully ingested {file_name} - {len(chunks)} chunks")
        except Exception as e:
            print(f"✗ Error ingesting {file_name}: {e}")

if __name__ == "__main__":
    asyncio.run(ingest_all_files())
