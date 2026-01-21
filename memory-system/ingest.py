import os
import json
import logging
import time
from datetime import datetime
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
load_dotenv(os.path.join(os.path.dirname(__file__), "../mcp-servers/google_workspace_mcp/.env")) # Try to load from MCP env too

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GRANOLA_CACHE_PATH = os.path.expanduser("~/Library/Application Support/Granola/cache-v3.json")
INDEX_NAME = "digital-brain-memory"

def get_embedding_model():
    logger.info("Loading embedding model...")
    return SentenceTransformer('all-MiniLM-L6-v2')

def setup_pinecone():
    if not PINECONE_API_KEY:
        logger.error("PINECONE_API_KEY not found in environment variables.")
        return None
    
    pc = Pinecone(api_key=PINECONE_API_KEY)
    
    # Check if index exists, create if not
    existing_indexes = pc.list_indexes().names()
    if INDEX_NAME not in existing_indexes:
        logger.info(f"Creating index: {INDEX_NAME}")
        pc.create_index(
            name=INDEX_NAME,
            dimension=384, # Dimensions for all-MiniLM-L6-v2
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )
    return pc.Index(INDEX_NAME)

def ingest_granola(index, model):
    if not os.path.exists(GRANOLA_CACHE_PATH):
        logger.warning(f"Granola cache not found at {GRANOLA_CACHE_PATH}")
        return

    logger.info(f"Reading Granola cache from {GRANOLA_CACHE_PATH}...")
    try:
        with open(GRANOLA_CACHE_PATH, 'r') as f:
            raw_data = json.load(f)
            
        # Parse nested inner JSON string
        if isinstance(raw_data, dict) and 'cache' in raw_data and isinstance(raw_data['cache'], str):
             inner_data = json.loads(raw_data['cache'])
             state = inner_data.get('state', {})
             documents = state.get('documents', {})
             
             # Convert dict of docs to list
             if isinstance(documents, dict):
                 meetings = list(documents.values())
             elif isinstance(documents, list):
                 meetings = documents
             else:
                 meetings = []
        else:
             # Fallback to previous logic just in case
             logger.warning("Cache structure unknown, falling back to raw iteration")
             meetings = raw_data if isinstance(raw_data, list) else []

        logger.info(f"Found {len(meetings)} items in Granola cache.")
        
        batch_size = 50
        vectors = []
        
        for meeting in meetings:
            # Extract relevant fields
            title = meeting.get('title', 'Untitled Meeting')
            date_str = meeting.get('created_at', datetime.now().isoformat())
            meeting_id = meeting.get('id', f"granola_{hash(title)}")

            # Text to embed
            text_parts = [f"Title: {title}"]
            
            summary = meeting.get('summary')
            if summary:
                text_parts.append(f"Summary: {summary}")
            
            overview = meeting.get('overview')
            if overview:
                text_parts.append(f"Overview: {overview}")

            notes = meeting.get('notes_plain') or meeting.get('notes_markdown')
            if notes:
                text_parts.append(f"Notes: {str(notes)[:2000]}") # Truncate long notes
                
            text = "\n".join(text_parts)
            
            if len(text) < 20: # Skip empty/short
                continue
            
            # Embed
            embedding = model.encode(text).tolist()
            
            vectors.append({
                "id": f"granola_{meeting_id}",
                "values": embedding,
                "metadata": {
                    "source": "granola",
                    "type": "meeting",
                    "title": title,
                    "date": str(date_str),
                    "text": text[:4000] # Limit metadata size
                }
            })
            
            if len(vectors) >= batch_size:
                logger.info(f"Upserting batch of {len(vectors)}...")
                index.upsert(vectors=vectors, namespace="meetings")
                vectors = []
                
        if vectors:
            logger.info(f"Upserting final batch of {len(vectors)}...")
            index.upsert(vectors=vectors, namespace="meetings")
            
        logger.info("Granola ingestion complete.")

    except Exception as e:
        logger.error(f"Error ingesting Granola: {e}")

def main():
    logger.info("Starting memory ingestion...")
    
    pc_index = setup_pinecone()
    if not pc_index:
        logger.error("Failed to setup Pinecone. Exiting.")
        return

    model = get_embedding_model()
    
    # 1. Ingest Granola
    ingest_granola(pc_index, model)
    
    # 2. Ingest WhatsApp (Placeholder)
    # logger.info("WhatsApp ingestion not implemented yet.")
    
    # 3. Ingest Gmail/Cal (Placeholder)
    # logger.info("Gmail/Calendar ingestion not implemented yet.")
    
    logger.info("Ingestion run finished.")

if __name__ == "__main__":
    main()
