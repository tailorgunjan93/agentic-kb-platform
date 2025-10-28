"""Test FAISS search endpoint"""
import urllib.parse
import urllib.request
import json

# Test parameters
queries = [
    "machine learning",
    "knowledge base",
    "artificial intelligence",
    "database systems"
]

print("Testing FAISS search endpoint...")
print("=" * 60)

for i, query in enumerate(queries):
    # Encode query
    encoded_query = urllib.parse.quote(query)
    url = f"http://127.0.0.1:8000/faiss/faiss_search?query={encoded_query}"
    
    print(f"\nTest {i+1}: {query}")
    print(f"URL: {url}")
    
    try:
        # Send request
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())
        
        # Print results
        print(f"✅ Found {len(data)} results")
        for j, result in enumerate(data[:3]):  # Show top 3
            print(f"  Result {j+1}: Score={result['score']:.4f}")
            print(f"    File: {result['filename']} (ID: {result['file_id']})")
            print(f"    Text: {result['text'][:100]}...")
            
    except Exception as e:
        print(f"❌ Error: {type(e).__name__}: {e}")

print("\n" + "=" * 60)
print("✅ All tests completed!")
print("=" * 60)
