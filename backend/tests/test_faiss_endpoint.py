"""Functional test for /faiss/faiss_search endpoint"""
import asyncio
from httpx import AsyncClient, ASGITransport
from main import app

async def run_tests():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as client:
        queries = [
            "machine learning",
            "knowledge base",
            "artificial intelligence",
        ]
        for query in queries:
            print("\nQuery:", query)
            resp = await client.get("/faiss/faiss_search", params={"query": query}, timeout=120)
            print("Status:", resp.status_code)
            if resp.status_code == 200:
                data = resp.json()
                print(f"Results returned: {len(data)}")
                if data:
                    top = data[0]
                    print("Top result score:", top.get("score"))
                    print("Top result file:", top.get("filename"))
            else:
                print("Error payload:", resp.text)

if __name__ == "__main__":
    asyncio.run(run_tests())
