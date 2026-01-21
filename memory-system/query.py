import os
import sys
from dotenv import load_dotenv
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

# Setup logging
import logging
logging.basicConfig(level=logging.ERROR)

def query_memory(query_text):
    # Load env
    load_dotenv()
    load_dotenv(os.path.join(os.path.dirname(__file__), "../mcp-servers/google_workspace_mcp/.env"))
    
    api_key = os.getenv("PINECONE_API_KEY")
    if not api_key:
        print("Error: PINECONE_API_KEY not found.")
        return

    # Connect
    pc = Pinecone(api_key=api_key)
    index_name = "digital-brain-memory"
    index = pc.Index(index_name)

    # Embed
    model = SentenceTransformer('all-MiniLM-L6-v2')
    vector = model.encode(query_text).tolist()

    # Query
    results = index.query(
        vector=vector,
        top_k=5,
        include_metadata=True,
        namespace="whatsapp" # Searching WhatsApp specifically for demo, or remove for all
    )

    print(f"\nResults for '{query_text}':\n")
    for match in results['matches']:
        meta = match['metadata']
        score = match['score']
        print(f"[{score:.2f}] {meta.get('source', 'unknown')} | {meta.get('date', 'no-date')}")
        print(f"Content: {meta.get('text', '')[:200]}...")
        print("-" * 40)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 query.py 'your query'")
        sys.exit(1)
    
    query_memory(sys.argv[1])
