"""Test the actual API endpoint"""
import urllib.request
import json
import time

# Wait a moment for server to start
print("Waiting for server to start...")
time.sleep(3)

print("Testing GET /api/test-chunks...")
try:
    response = urllib.request.urlopen('http://127.0.0.1:8000/api/test-chunks', timeout=30)
    data = json.loads(response.read().decode())
    
    print("\n✅ API Response:")
    print(f"  Success: {data.get('success')}")
    print(f"  Chunk count: {data.get('count')}")
    
    if data.get('chunks'):
        print(f"  Sample chunk: {data['chunks'][0] if len(data['chunks']) > 0 else 'None'}")
    
    if data.get('error'):
        print(f"  Error: {data.get('error')}")
        print(f"  Type: {data.get('type')}")
    
except urllib.error.HTTPError as e:
    print(f"❌ HTTP Error {e.code}: {e.reason}")
    print(f"Response: {e.read().decode()}")
except Exception as e:
    print(f"❌ Error: {type(e).__name__}: {e}")
