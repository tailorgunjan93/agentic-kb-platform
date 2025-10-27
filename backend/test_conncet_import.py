"""Test importing db.conncet module to see what DATABASE_URL it creates"""
import sys
print("Testing db.conncet import...")
print("="*60)

# Import the module
from db import conncet

print("\n" + "="*60)
print("Import successful!")
print(f"Engine: {conncet.engine}")
print(f"Engine URL: {conncet.engine.url}")
