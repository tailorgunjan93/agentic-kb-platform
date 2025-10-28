"""Test the optimized API endpoints"""
import urllib.request
import json
import time

def test_endpoint(url, name):
    """Test an endpoint and measure response time"""
    print(f"\n{'='*60}")
    print(f"Testing: {name}")
    print(f"URL: {url}")
    print('='*60)
    
    start = time.time()
    try:
        response = urllib.request.urlopen(url, timeout=60)
        data = json.loads(response.read().decode())
        elapsed = time.time() - start
        
        print(f"✅ Response time: {elapsed:.2f}s")
        print(f"Success: {data.get('success')}")
        
        if 'total' in data:
            print(f"Total chunks: {data.get('total')}")
            print(f"Returned: {data.get('count')}")
        elif 'count' in data:
            print(f"Chunk count: {data.get('count')}")
        
        if data.get('chunks'):
            sample = data['chunks'][0] if len(data['chunks']) > 0 else None
            if sample:
                print(f"Sample chunk: {list(sample.keys())}")
        
        return elapsed
        
    except Exception as e:
        elapsed = time.time() - start
        print(f"❌ Error after {elapsed:.2f}s: {type(e).__name__}: {e}")
        return elapsed

# Wait for server
print("Waiting for server startup...")
time.sleep(2)

# Test 1: Health check (should be instant)
test_endpoint('http://127.0.0.1:8000/api/health', 'Health Check')

# Test 2: Fast chunks endpoint with pagination (should be fast with cache)
test_endpoint('http://127.0.0.1:8000/api/chunks?limit=10', 'Get 10 Chunks (Cached)')

# Test 3: Get more chunks
test_endpoint('http://127.0.0.1:8000/api/chunks?limit=100&offset=100', 'Get 100 Chunks with Offset')

# Test 4: Test chunks with cache (should be fast after first build)
test_endpoint('http://127.0.0.1:8000/api/test-chunks', 'Test Chunks (Cached)')

print(f"\n{'='*60}")
print("✅ All tests completed!")
print('='*60)
