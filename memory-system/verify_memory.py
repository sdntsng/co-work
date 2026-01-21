import os
import sys
from dotenv import load_dotenv
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

# Load env
load_dotenv()
api_key = os.getenv("PINECONE_API_KEY")

if not api_key:
    print("Error: No API key found.")
    sys.exit(1)

pc = Pinecone(api_key=api_key)
index_name = "digital-brain-memory"

if index_name not in pc.list_indexes().names():
    print(f"Error: Index {index_name} does not exist.")
    sys.exit(1)

index = pc.Index(index_name)

# Check stats
stats = index.describe_index_stats()
print("Index Stats:", stats)

# Simple query
print("\nQuerying 'meeting'...")
model = SentenceTransformer('all-MiniLM-L6-v2')
emb = model.encode("meeting", normalize_embeddings=True).tolist()

results = index.query(
    vector=emb,
    top_k=3,
    namespace="meetings",
    include_metadata=True
)

print(f"Found {len(results.matches)} matches in 'meetings' namespace.")
for m in results.matches:
    print(f"- {m.score:.2f}: {m.metadata.get('title', 'No Title')}")
