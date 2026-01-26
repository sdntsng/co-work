#!/bin/bash
# MCP Servers Shutdown Script for co-work
# Stops background MCP services

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}🛑 Stopping MCP Services...${NC}"

# Stop new WhatsApp (Go implementation)
if pgrep -f "whatsapp-fiber/whatsapp" > /dev/null; then
    pkill -f "whatsapp-fiber/whatsapp"
    echo -e "${GREEN}✅ Stopped WhatsApp MCP (frontend/SSE)${NC}"
else
    echo -e "${YELLOW}⚠️  WhatsApp MCP was not running${NC}"
fi

# Stop old WhatsApp bridge (just in case)
if pgrep -f "whatsapp-bridge" > /dev/null; then
    pkill -f "whatsapp-bridge"
    echo -e "${GREEN}✅ Stopped legacy WhatsApp bridge${NC}"
fi

echo -e "${GREEN}✅ All background MCP services stopped.${NC}"
