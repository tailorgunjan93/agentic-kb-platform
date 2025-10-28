"""Test if password special characters need encoding"""
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from urllib.parse import quote_plus

async def test():
    # Original password: Gun@123!
    password = "Gun@123!"
    encoded_password = quote_plus(password)
    
    print(f"Original password: {password}")
    print(f"URL encoded password: {encoded_password}")
    
    url1 = f"postgresql+asyncpg://postgres:{password}@127.0.0.1:5432/agentic_kb"
    url2 = f"postgresql+asyncpg://postgres:{encoded_password}@127.0.0.1:5432/agentic_kb"
    
    print(f"\nURL 1 (unencoded): {url1}")
    print(f"URL 2 (encoded): {url2}")
    
    print("\nTest 1: Unencoded password")
    try:
        engine = create_async_engine(url1, echo=False)
        async with engine.begin() as conn:
            from sqlalchemy import text
            await conn.execute(text("SELECT 1"))
            print("✅ Success!")
        await engine.dispose()
    except Exception as e:
        print(f"❌ Failed: {type(e).__name__}: {str(e)[:100]}")
    
    print("\nTest 2: URL-encoded password")
    try:
        engine = create_async_engine(url2, echo=False)
        async with engine.begin() as conn:
            from sqlalchemy import text
            await conn.execute(text("SELECT 1"))
            print("✅ Success!")
        await engine.dispose()
    except Exception as e:
        print(f"❌ Failed: {type(e).__name__}: {str(e)[:100]}")

if __name__ == "__main__":
    asyncio.run(test())
