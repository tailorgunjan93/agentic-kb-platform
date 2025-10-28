"""Test direct asyncpg connection"""
import asyncio
import asyncpg

async def test_connection():
    print("Testing direct asyncpg connection...")
    print(f"Host: 127.0.0.1")
    print(f"Port: 5432")
    print(f"User: postgres")
    print(f"Database: agentic_kb")
    
    try:
        conn = await asyncpg.connect(
            host='127.0.0.1',
            port=5432,
            user='postgres',
            password='Gun@123!',
            database='agentic_kb'
        )
        print("✅ Connection successful!")
        
        # Test a simple query
        result = await conn.fetchval('SELECT version()')
        print(f"PostgreSQL version: {result}")
        
        await conn.close()
        print("Connection closed successfully")
    except Exception as e:
        print(f"❌ Connection failed: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_connection())
