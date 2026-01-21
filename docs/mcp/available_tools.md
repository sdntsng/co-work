# Perplexity MCP

**Server:** `perplexity-ask`
**Source:** `server-perplexity-ask` (npm)

## Capabilities
- **Search**: Perform deep research queries on the web.
- **Context**: Returns sourced answers suitable for technical or general research.

## Configuration
Requires `PERPLEXITY_API_KEY`.

---

# GitHub (Gemini Extension)

**Extension:** `github`
**Source:** `https://github.com/github/github-mcp-server`

## Capabilities
- **Remote MCP**: Connects to `https://api.githubcopilot.com/mcp/`.
- **Repository Management**: Read file contents, list files.
- **Issues & PRs**: Create, read, and manage issues/pull requests.

---

# Pinecone (Gemini Extension)

**Extension:** `pinecone-mcp`
**Source:** `https://github.com/pinecone-io/pinecone-mcp`

## Capabilities
- **Vector Database**: Manage indexes and query vector data.
- **MCP Server**: Runs `@pinecone-database/mcp`.

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
