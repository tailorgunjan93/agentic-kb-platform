"""Configuration helpers for environment loading and logging setup."""

import logging
from dotenv import load_dotenv
import os
from pathlib import Path

# Locate the root-level .env file so backend scripts can share credentials.
env_path = Path(__file__).parent.parent/".env"
load_dotenv(override=True)

DB_CONFIG = {
    # Connection parameters pulled from environment for security.
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT","5432")),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "dbname": os.getenv("DB_NAME")
}

def setup_logger(name="ingestion"):
    """Create a namespaced logger with the project's default formatting."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )
    return logging.getLogger(name)