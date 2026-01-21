# Agentic Operations Protocol

## Objective
Enable the AI Agent to perform Google Workspace operations and maintain the application codebase based on natural language requests.

## Core Principle
"You talk, I execute."

---

## 1. MCP Registry

| Operation | Source |
|-----------|---------|
| Web Search | `perplexity-ask` (MCP) |
| GitHub | `github-mcp-server` (MCP) |
| Workspace | `google-workspace` (Extension) |

---

## 2. Google Workspace Utils (Legacy/Archive)

| Operation | Command |
|-----------|---------|
| List sheets | `./venv/bin/python -m src.main list-sheets` |
| Read data | `./venv/bin/python -m src.main read-data "Sheet Name" "Tab Name"` |
| Update cell | `./venv/bin/python -m src.main update-cell "Sheet" "A1" "value"` |
| Append row | `./venv/bin/python -m src.main append-row "Sheet" "val1,val2"` |

---

## 2. Development Rules
- **Runtime**: Python 3.13 (`venv`).
- **Entry Point**: `src.main`.
- **Commits**: Incremental, descriptive scope (e.g., `feat(core): ...`, `fix(auth): ...`).
- **Dependencies**: `requirements.txt`