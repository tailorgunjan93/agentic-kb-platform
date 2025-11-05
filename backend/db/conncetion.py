from config import DB_CONFIG
import psycopg2
import asyncpg
from urllib.parse import quote_plus
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent.parent.parent/".env"
load_dotenv(dotenv_path=env_path)
# URL-encode password to handle special characters like @ and !
password = quote_plus("Gun@123!")


DATABASE_URL = (
    f"postgresql://postgres:{password}"
    f"@db:5432/agentic_kb"
)

pool =psycopg2.connect(DATABASE_URL)

def get_conncetion():
    return pool

def release_connection(conn):
    if pool:
        return conn.close()