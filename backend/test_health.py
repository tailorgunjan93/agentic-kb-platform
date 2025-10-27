"""Test the health check endpoint"""
import urllib.request
import json

print("Testing GET /api/health...")
try:
    response = urllib.request.urlopen('http://127.0.0.1:8000/api/health', timeout=5)
    data = json.loads(response.read().decode())
    
    print("\n✅ Health Check Response:")
    print(json.dumps(data, indent=2))
    
except Exception as e:
    print(f"❌ Error: {type(e).__name__}: {e}")
