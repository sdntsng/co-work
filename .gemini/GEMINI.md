# Gemini CLI Agent Context

## 1. Project Overview
**Project**: Digital Brain (MCP Workspace)
**User**: Sid
**Goal**: A centralized "Operating System" for day-to-day work, driven by the Model Context Protocol (MCP).

## 2. Reference Library
The following files define the operational bounds and capabilities of this agent.

### 📜 Rules (Constraints & Standards)
- **[docs/rules/agent-operation.md](docs/rules/agent-operation.md)**: MCP-centric protocols and "You Talk, I Execute" philosophy.
- **[.agent/rules/design_system.md](.agent/rules/design_system.md)**: "Digital Paper" UI standards (Typography, Colors, Spacing).

### 🛠 MCP Configuration & Tools
- **[mcp_config.json](mcp_config.json)**: Main MCP server definitions (Perplexity, GitHub).
- **[docs/mcp/available_tools.md](docs/mcp/available_tools.md)**: Detailed documentation of available MCP capabilities.

### 🗺 Roadmap
- **[docs/tasks.md](docs/tasks.md)**: Current active task list and backlog.

---

## 3. Current System Capabilities
*System powered by MCP Servers and Extensions.*

### Configured MCP Servers
- **Perplexity Ask**: Deep research and web search.
- **GitHub**: Repository management, Issues, and Pull Requests.
- **Google Workspace (Extension)**: Integrated Google Workspace tools via `gemini-cli-extensions/workspace`.

---

## 4. Archive
- **[archive/](archive/)**: Legacy Python codebase for Google Workspace automation.
