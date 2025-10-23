import logging

DB_CONFIG = {
    'dbname': 'agentic_kb',
    'user': 'postgres',
    'password': 'Gun@123!',  # Replace with secure credential
    'host': 'localhost',
    'port': 5432
}

def setup_logger(name="ingestion"):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )
    return logging.getLogger(name)