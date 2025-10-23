import logging
from dotenv import load_dotenv
import os

load_dotenv()
# DB_CONFIG = {
#     'dbname': "agentic_kb",
#     'user': "postgres",
#     'password': "Gun@123!",
#     'host': "localhost",
#     'port': 5432
# }

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