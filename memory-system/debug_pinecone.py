import os
import sys
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()
api_key = os.getenv("PINECONE_API_KEY")
pc = Pinecone(api_key=api_key)

print("Listing indexes...")
indexes = pc.list_indexes()
print(f"Raw indexes object: {indexes}")

# In v3, list_indexes returns IndexList object which is iterable of IndexModel?
try:
    names = [i.name for i in indexes]
    print(f"Index Names: {names}")
except:
    print("Could not iterate indexes.")

index_name = "digital-brain-memory"
if index_name in names:
    print("Index found!")
    idx = pc.Index(index_name)
    print(idx.describe_index_stats())
else:
    print("Index NOT found.")
