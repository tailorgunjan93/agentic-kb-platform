"""Test the API endpoint logic directly"""
import asyncio
from db.conncet import get_session
from db.quries import fetch_all_chunks

async def test():
    print("Testing fetch_all_chunks...")
    try:
        # Get a session
        async for db in get_session():
            print(f"Got database session: {db}")
            
            # Try to fetch chunks
            chunks = await fetch_all_chunks(db)
            print(f"✅ Success! Fetched {len(chunks)} chunks")
            if chunks:
                print(f"Sample chunk: {chunks[0]}")
            else:
                print("No chunks found in database")
            break
    except Exception as e:
        print(f"❌ Error: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test())
