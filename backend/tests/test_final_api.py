"""Test the complete API flow"""
import asyncio
import sys

async def test():
    print("=" * 60)
    print("Testing API Flow")
    print("=" * 60)
    
    # Test 1: Import models
    print("\n1. Testing model imports...")
    try:
        from models.chunk import Embeddings
        from models.file import File
        print(f"✅ Embeddings model: {Embeddings.__tablename__}")
        print(f"✅ File model: {File.__tablename__}")
        print(f"   Embeddings columns: {[c.name for c in Embeddings.__table__.columns]}")
        print(f"   File columns: {[c.name for c in File.__table__.columns]}")
    except Exception as e:
        print(f"❌ Model import failed: {e}")
        import traceback
        traceback.print_exc()
        return
    
    # Test 2: Database connection
    print("\n2. Testing database connection...")
    try:
        from db.conncet import get_session
        db = await anext(get_session())
        print(f"✅ Database session created: {db}")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        import traceback
        traceback.print_exc()
        return
    
    # Test 3: Fetch chunks
    print("\n3. Testing fetch_all_chunks...")
    try:
        from db.quries import fetch_all_chunks
        chunks = await fetch_all_chunks(db)
        print(f"✅ Fetched {len(chunks)} chunks")
        if chunks:
            print(f"   Sample chunk: {chunks[0]}")
    except Exception as e:
        print(f"❌ Fetch chunks failed: {e}")
        import traceback
        traceback.print_exc()
        return
    
    # Test 4: Build FAISS index
    print("\n4. Testing build_faiss_index...")
    try:
        from vectorstore.index import build_faiss_index
        result = await build_faiss_index()
        print(f"✅ FAISS index built with {len(result) if result else 0} chunks")
    except Exception as e:
        print(f"❌ FAISS index build failed: {e}")
        import traceback
        traceback.print_exc()
        return
    
    print("\n" + "=" * 60)
    print("✅ All tests passed!")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(test())
