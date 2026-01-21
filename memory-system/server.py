import os
from mcp.server.fastmcp import FastMCP
from pinecone import Pinecone
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("memory-mcp")

# Initialize Pinecone
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index_name = "digital-brain-memory"

@mcp.tool()
def search_memory(query: str, limit: int = 5) -> str:
    """
    Search your external memory (meetings, chats, emails) for relevant information.
    Use this to recall facts, conversations, or details from the past.
    """
    try:
        # Check if index exists
        if index_name not in pc.list_indexes().names():
            return "Memory index not found. Please run ingestion first."

        index = pc.Index(index_name)

        # Generate embedding for query (using same model as ingestion)
        # For simplicity in this demo, we assume the same model "multilingual-e5-large"
        # In production, we'd use a shared embedding service or local lib
        # Here we use Pinecone's inference if available, or just standard OpenAI/similar
        
        # ACTUALLY: To keep it simple and consistent with ingestion (which will use OpenAI or Local),
        # let's assume we use OpenAI for now as it's cleaner for the 'server' component 
        # to not have heavy local dep dependencies if possible, BUT plan said local.
        # So we import the same embedding logic.
        
        from sentence_transformers import SentenceTransformer
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Embed query
        query_embedding = model.encode(query, normalize_embeddings=True).tolist()

        # Query Pinecone
        results = index.query(
            vector=query_embedding,
            top_k=limit,
            include_metadata=True
        )

        # Format results
        response = f"Found {len(results.matches)} relevant memories:\n\n"
        for match in results.matches:
            source = match.metadata.get('source', 'unknown')
            text = match.metadata.get('text', '')
            date = match.metadata.get('date', 'unknown')
            score = match.score
            response += f"- [{source}] ({date}) {text} (Confidence: {score:.2f})\n"

        return response

    except Exception as e:
        return f"Error searching memory: {str(e)}"

if __name__ == "__main__":
    mcp.run()
