import os
from pathlib import Path
from dotenv import load_dotenv

# Test 1: Check current directory
print(f"Current file: {__file__}")
print(f"Current directory: {os.getcwd()}")

# Test 2: Calculate env path
env_path = Path(__file__).parent.parent / ".env"
print(f"\nCalculated .env path: {env_path}")
print(f"Absolute path: {env_path.absolute()}")
print(f"File exists: {env_path.exists()}")

# Test 3: Load environment variables
if env_path.exists():
    print(f"\n.env file contents:")
    with open(env_path, 'r') as f:
        print(f.read())
    
    load_dotenv(dotenv_path=env_path)
    print(f"\nLoaded environment variables:")
    print(f"DB_HOST: {os.getenv('DB_HOST')}")
    print(f"DB_PORT: {os.getenv('DB_PORT')}")
    print(f"DB_USER: {os.getenv('DB_USER')}")
    print(f"DB_PASSWORD: {os.getenv('DB_PASSWORD')}")
    print(f"DB_NAME: {os.getenv('DB_NAME')}")
    
    # Test 4: Build connection string
    DATABASE_URL = (
        f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    print(f"\nDATABASE_URL: {DATABASE_URL}")
else:
    print("\n❌ .env file not found!")

# Test 5: Test path from db/conncet.py perspective
print("\n" + "="*50)
print("Testing from db/conncet.py perspective:")
db_file_path = Path(__file__).parent / "db" / "conncet.py"
print(f"Simulated conncet.py path: {db_file_path}")
env_path_from_db = db_file_path.parent.parent.parent / ".env"
print(f"Calculated .env path from db/: {env_path_from_db}")
print(f"Absolute path: {env_path_from_db.absolute()}")
print(f"File exists: {env_path_from_db.exists()}")
