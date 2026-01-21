# MCP Registry & Configuration

This repository is now a dedicated configuration and documentation hub for **Model Context Protocol (MCP)** integration.

## Active MCP Servers

Configuration file: `mcp_config.json`

| Server Name | Type | Description |
| :--- | :--- | :--- |
| **perplexity-ask** | Search | Provides internet search capabilities via Perplexity API. |
| **github-mcp-server** | Integration | Allows interaction with GitHub repositories (Issues, PRs, etc.). |

## Usage

This repository is intended to be used with an MCP Client (like Claude Desktop, or a custom agent).

### Quick Start

1. Ensure `npx` is available in your path.
2. Verify API keys in `mcp_config.json` (Note: Ensure `mcp_config.json` is **NOT** committed if it contains real secrets).

## Directory Structure

*   `mcp_config.json`: Main configuration file defining servers.
*   `docs/mcp/`: Documentation for specific MCP workflows and capabilities.
*   `archive/`: Legacy Python codebase (Sheets/Drive automation).
