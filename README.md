# Digital Brain (Co-Work Workspace)

A comprehensive MCP-powered "Operating System" for work, acting as a bridge between an AI Agent (Claude/Gemini) and your personal data (WhatsApp, Granola, Google Workspace).

## 🧠 Architecture

The system consists of three main layers:

### 1. The Memory System (Long-Term Storage)
A continuous ingestion pipeline that indexes your life into a Vector Database (Pinecone), making it searchable by AI.

*   **Ingestion Script (`memory-system/ingest.py`)**: Runs hourly.
    *   **Granola**: Reads meeting intelligence (Summaries, Takeaways, Transcripts, Action Items) from the local cache.
    *   **WhatsApp**: Reads direct from local SQLite database (`messages.db`), grouping chats by day. Filtering for last 90 days.
*   **Vector DB**: Pinecone (Serverless AWS) stores semantic embeddings of all this data.

### 2. The MCP Layer (Real-Time Actions)
A unified suite of servers that allow the AI to **act** on your behalf. All managed in `mcp-servers/`.

| Server | Type | Purpose | Capability |
| :--- | :--- | :--- | :--- |
| **memory-mcp** | Custom (Python) | Retrieval | `search_memory(query)` - Search your Digital Brain. |
| **whatsapp-mcp** | Docker (Go) | Messaging | Send/Receive messages, list chats, search history. |
| **granola-mcp** | Custom (Python) | Meetings | Access structured notes and transcripts. |
| **gworkspace** | Python | Productivity | Gmail, Calendar, Drive, Docs automation. |
| **perplexity** | Standard | Research | Web search and deep research. |
| **github** | Standard | Engineering | Repository management. |

### 3. The Agent Layer (Interface)
This is where YOU interact. Returns a fully contextualized agent that knows:
*   What you said on WhatsApp yesterday.
*   What was decided in the meeting last week.
*   Your schedule and emails.

---

## 🚀 Quick Start

### 1. Prerequisites
*   **Docker Desktop** (Required for WhatsApp)
*   **Python 3.12+** (For Memory System & Custom MCPs)
*   **Pinecone Account** (API Key)

### 2. Installation
```bash
# 1. Clone & Setup Deps
cd co-work
./mcp-servers/scripts/start-mcp.sh  # Installs python deps & checks environment

# 2. Start WhatsApp (if not running)
docker start whatsapp-mcp
# Note: First run requires scanning QR code (view with `docker logs whatsapp-mcp`)
```

### 3. Usage

#### 🧠 Querying Memory
You can ask the agent directly, or use the CLI for debugging:
```bash
python3 memory-system/query.py "What did I discuss with Neeraj regarding the venue?"
```

#### 💬 WhatsApp
To link a new device:
```bash
docker logs -f whatsapp-mcp
# Scan the QR code displayed in the terminal
```

#### 🔄 Manual Ingestion
To force an immediate update of your memory bank:
```bash
python3 memory-system/ingest.py
```

---

## Directory Structure
```
co-work/
├── .gemini/                  # Agent brain & settings
├── mcp-servers/              # MCP Server Implementations
│   ├── .venv/                # Shared Python Environment
│   ├── whatsapp-mcp/         # WhatsApp Server (Docker)
│   ├── granola_mcp/          # Granola Meeting Server
│   └── google_workspace_mcp/ # Google Tools
├── memory-system/            # The "Brain" Logic
│   ├── ingest.py             # Data Pipeline (Granola/WA -> Pinecone)
│   ├── server.py             # Memory Retrieval MCP
│   └── query.py              # CLI Debug Tool
└── docs/                     # Documentation
```
