from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Load .env from project root (two levels up from this file)
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(override=True)

# URL-encode password to handle special characters like @ and !
password = quote_plus(os.getenv('DB_PASSWORD'))

DATABASE_URL = (
    f"postgresql+asyncpg://{os.getenv('DB_USER')}:{password}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine,class_=AsyncSession,expire_on_commit=False)

async def get_session():
    async with async_session() as session:
        yield session