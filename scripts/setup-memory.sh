#!/bin/bash
# Setup script for Memory System

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="$PROJECT_ROOT/mcp-servers/.venv"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}🧠 Setting up Digital Brain Memory System...${NC}"

# 1. Install Dependencies
echo "📦 Installing Python dependencies..."
source "$VENV_DIR/bin/activate"
pip install -r "$PROJECT_ROOT/memory-system/requirements.txt"

# 2. Check for Pinecone API Key
if [ -z "$PINECONE_API_KEY" ]; then
    echo -e "${YELLOW}⚠️  PINECONE_API_KEY is not set in environment.${NC}"
    echo "Please add it to your .env file or export it before running ingestion."
    echo "Example: export PINECONE_API_KEY='your-key-here'"
fi

# 3. Cron Setup Instructions
CRON_CMD="0 */3 * * * cd $PROJECT_ROOT && $VENV_DIR/bin/python memory-system/ingest.py >> memory_ingest.log 2>&1"

echo ""
echo -e "${GREEN}✅ Setup Complete!${NC}"
echo ""
echo "To enable automatic ingestion (every 3 hours), add this line to your crontab:"
echo "-----------------------------------------------------------------------------"
echo "$CRON_CMD"
echo "-----------------------------------------------------------------------------"
echo "Run 'crontab -e' to edit."
echo ""
echo "To run manually now:"
echo "cd $PROJECT_ROOT && $VENV_DIR/bin/python memory-system/ingest.py"
