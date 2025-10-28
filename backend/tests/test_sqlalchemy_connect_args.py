"""Test SQLAlchemy with different connection parameters"""
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

DATABASE_URL = (
    f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
print(f"DATABASE_URL: {DATABASE_URL}")

async def test_connection():
    print("\nTest 1: With ssl=False in connect_args")
    try:
        engine = create_async_engine(
            DATABASE_URL,
            echo=False,
            connect_args={"ssl": False}
        )
        async with engine.begin() as conn:
            result = await conn.execute("SELECT 1")
            print("✅ Connection successful!")
        await engine.dispose()
    except Exception as e:
        print(f"❌ Failed: {type(e).__name__}: {e}")
    
    print("\nTest 2: With server_settings in connect_args")
    try:
        engine = create_async_engine(
            DATABASE_URL,
            echo=False,
            connect_args={"server_settings": {"application_name": "test_app"}}
        )
        async with engine.begin() as conn:
            result = await conn.execute("SELECT 1")
            print("✅ Connection successful!")
        await engine.dispose()
    except Exception as e:
        print(f"❌ Failed: {type(e).__name__}: {e}")
    
    print("\nTest 3: No connect_args")
    try:
        engine = create_async_engine(
            DATABASE_URL,
            echo=False
        )
        async with engine.begin() as conn:
            result = await conn.execute("SELECT 1")
            print("✅ Connection successful!")
        await engine.dispose()
    except Exception as e:
        print(f"❌ Failed: {type(e).__name__}: {e}")

if __name__ == "__main__":
    asyncio.run(test_connection())
