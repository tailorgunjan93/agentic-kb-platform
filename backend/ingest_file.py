import fitz  # PyMuPDF
import psycopg2
import uuid
from datetime import datetime

# === CONFIG ===
DB_CONFIG = {
    'dbname': 'agentic_kb',
    'user': 'postgres',
    'password': 'your_password',
    'host': 'localhost',
    'port': 5432
}
FILE_PATH = 'backend/uploads/human-nutrition-text.pdf'
CHUNK_SIZE = 500  # characters per chunk

# === CONNECT TO DB ===
conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

# === GET USER & FILE ID ===
cur.execute("SELECT id FROM users WHERE email = %s", ('demo@agentic.ai',))
user_id = cur.fetchone()[0]

cur.execute("SELECT id FROM files WHERE filename = %s", ('human-nutrition-text.pdf',))
file_id = cur.fetchone()[0]

# === READ & CHUNK PDF ===
doc = fitz.open(FILE_PATH)
full_text = ""
for page in doc:
    full_text += page.get_text()

chunks = [full_text[i:i+CHUNK_SIZE] for i in range(0, len(full_text), CHUNK_SIZE)]

# === INSERT EMBEDDINGS ===
for idx, chunk in enumerate(chunks):
    dummy_vector = [round(0.001 * (i+1), 6) for i in range(1536)]  # Replace with real embedding
    cur.execute("""
        INSERT INTO embeddings (id, file_id, chunk_index, content, embedding, created_at)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        str(uuid.uuid4()), file_id, idx, chunk, dummy_vector, datetime.now()
    ))

conn.commit()
cur.close()
conn.close()
print(f"Ingested {len(chunks)} chunks from {FILE_PATH}")