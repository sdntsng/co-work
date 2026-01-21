# MCP Registry & Configuration

This repository is now a dedicated configuration and documentation hub for **Model Context Protocol (MCP)** integration.

## Active MCP Servers

Configuration file: `.gemini/settings.json`

| Server Name | Type | Description |
| :--- | :--- | :--- |
| **perplexity-ask** | Search | Provides internet search capabilities via Perplexity API. |
| **github** | Extension | Allows interaction with GitHub repositories (Issues, PRs, etc.). |
| **pinecone** | Extension | Vector database management. |
| **google-workspace** | Extension | Sheets, Drive, Docs integration. |

## Usage

This repository is intended to be used with an MCP Client (like Claude Desktop, or a custom agent).

### Quick Start

1. Ensure `npx` is available in your path.
2. Verify API keys in `.gemini/settings.json` (Note: Ensure `.gemini/settings.json` is **NOT** committed if it contains real secrets).

## Directory Structure

*   `.gemini/settings.json`: Workspace configuration file defining MCP servers.
*   `docs/mcp/`: Documentation for specific MCP workflows and capabilities.
*   `archive/`: Legacy Python codebase (Sheets/Drive automation).
