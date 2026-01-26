#!/bin/bash
# MCP Servers Startup Script for co-work
# Sets up venv and starts all required services

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MCP_DIR="$(dirname "$SCRIPT_DIR")"
VENV_DIR="$MCP_DIR/.venv"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}       MCP Servers - co-work Digital Brain       ${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Setup venv if not exists
if [ ! -d "$VENV_DIR" ]; then
    echo -e "${YELLOW}📦 Creating Python virtual environment...${NC}"
    python3 -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"
    pip install -e "$MCP_DIR/GranolaMCP/"
    pip install -e "$MCP_DIR/google_workspace_mcp/"
    echo -e "${GREEN}✅ Virtual environment ready${NC}"
else
    source "$VENV_DIR/bin/activate"
    echo -e "${GREEN}✅ Virtual environment activated${NC}"
fi

echo ""

# Check if WhatsApp MCP is already running
if pgrep -f "whatsapp-fiber/whatsapp mcp" > /dev/null; then
    echo -e "${YELLOW}📱 WhatsApp MCP already running on port 8080${NC}"
else
    echo -e "${GREEN}📱 Starting WhatsApp MCP (SSE)...${NC}"
    # Use proper nohup to detach process so it survives terminal closing
    nohup "$MCP_DIR/whatsapp-fiber/whatsapp" mcp --port 8080 > "$MCP_DIR/whatsapp.log" 2>&1 &
    WHATSAPP_PID=$!
    echo "   PID: $WHATSAPP_PID"
    echo "   Log: $MCP_DIR/whatsapp.log"
fi

    echo "   Log: $MCP_DIR/whatsapp.log"
fi

echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ MCP Services Ready!${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "Available MCP Servers:"
echo "  📧 gworkspace-vinci     (s@tryvinci.com)"
echo "  📧 gworkspace-engram    (siddhant@engramhq.com)"
echo "  📧 gworkspace-personal  (s9522565616@gmail.com)"
echo "  📝 granola-mcp          (meeting notes)"
echo "  💬 whatsapp             (http://localhost:8080/sse)"
echo "  🔍 perplexity-ask       (web search)"
echo "  🐙 github-mcp-server    (GitHub)"
echo "  📚 context7             (documentation)"
echo ""

# Keep script running to show logs if requested
echo -e "${YELLOW}💡 Run 'tail -f $MCP_DIR/whatsapp.log' to see WhatsApp logs${NC}"
echo ""
