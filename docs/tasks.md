# Project Roadmap & Tasks

## 1. Core Integrations (MCP)
- [ ] **Model Context Protocol (MCP)**: Integrate MCP to standardize tool use and context sharing.
    - [ ] Research and select initial MCP servers/tools.
    - [ ] Implement MCP client/host in `src/`.
- [ ] **Google Workspace**:
    - [x] Basic Sheets, Drive, Docs operations (`src/services/google`).
    - [ ] Enhance with MCP capability.

## 2. Core Features (The "Digital Brain")
- [ ] **Memory Layer**: Implement a persistence layer (SQLite/JSON) to store:
    - User preferences.
    - Context from previous sessions.
    - "Who am I" facts.
- [ ] **Unified Interface**: Update `main.py` to support natural language routing via MCP.

## 3. Future Roadmap
- [ ] **Knowledge Base**:
    - Integration with Granola (Meeting Notes).
    - Obsidian/Markdown note parsing.
- [ ] **Communication**:
    - Gmail/Email integration (read/draft).
    - WhatsApp Business API or web automation.

## 4. Documentation
- [ ] Maintain `docs/rules/` for operational constraints.
- [ ] Keep this `docs/tasks.md` updated with progress.