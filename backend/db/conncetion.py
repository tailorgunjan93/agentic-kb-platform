from config import DB_CONFIG
import psycopg2
import asyncpg

pool =psycopg2.connect(**DB_CONFIG)

def get_conncetion():
    return pool

def release_connection(conn):
    if pool:
        return conn.close()