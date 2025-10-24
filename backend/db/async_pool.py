import asyncpg
from config import DB_CONFIG
from pgvector.asyncpg import register_vector  # add this

db_pool = None
async def _init_connection(conn):
    await register_vector(conn)  # register codec on each connection

async def init_pool():
    global db_pool
    if db_pool is None:
        db_pool = await asyncpg.create_pool(
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["dbname"],
            min_size=1,
            max_size=10,
            init=_init_connection  # add this
        )

async def get_conncetion():
    global db_pool
    if db_pool is None:
        await init_pool()
    return await db_pool.acquire()

async def release_conncetion(conn):
    global db_pool
    if db_pool:
        db_pool.release(conn)
    