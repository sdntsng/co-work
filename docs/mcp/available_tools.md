# Perplexity MCP

**Server:** `perplexity-ask`
**Source:** `server-perplexity-ask` (npm)

## Capabilities
- **Search**: Perform deep research queries on the web.
- **Context**: Returns sourced answers suitable for technical or general research.

## Configuration
Requires `PERPLEXITY_API_KEY`.

---

# GitHub MCP

**Server:** `github-mcp-server`
**Source:** `@modelcontextprotocol/server-github` (npm)

## Capabilities
- **Repository Management**: Read file contents, list files.
- **Issues**: Create, read, update issues.
- **Pull Requests**: Review and manage PRs.

## Configuration
Requires `GITHUB_PERSONAL_ACCESS_TOKEN`.

---

# Google Workspace (Gemini Extension)

**Extension:** `google-workspace`
**Source:** `https://github.com/gemini-cli-extensions/workspace`

## Capabilities
- **Sheets**: Manage spreadsheets, read/write cells.
- **Drive**: Search and organize files.
- **Docs**: Read and create documents.
- **Gmail**: (If supported by the extension) Read and send emails.

## Configuration
Managed via `gemini extensions` command. Requires `credentials.json` for initial setup.
