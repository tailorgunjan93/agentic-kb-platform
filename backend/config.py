import logging
from dotenv import load_dotenv
import os
from pathlib import Path

# Load .env from project root (one level up from backend)
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "dbname": os.getenv("DB_NAME")
}

def setup_logger(name="ingestion"):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )
    return logging.getLogger(name)