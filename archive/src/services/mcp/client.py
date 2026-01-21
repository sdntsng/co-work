import json
import os
import shutil
from typing import Dict, Any, List, Optional
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from contextlib import AsyncExitStack

class MCPManager:
    def __init__(self, config_path: str = "mcp_config.json"):
        self.config_path = config_path
        self.servers: Dict[str, Any] = {}
        self.sessions: Dict[str, ClientSession] = {}
        self.exit_stack = AsyncExitStack()

    def load_config(self) -> Dict[str, Any]:
        if not os.path.exists(self.config_path):
            return {}
        with open(self.config_path, "r") as f:
            return json.load(f)

    async def connect(self):
        config = self.load_config()
        mcp_servers = config.get("mcpServers", {})

        for name, server_config in mcp_servers.items():
            command = server_config.get("command")
            args = server_config.get("args", [])
            env = server_config.get("env", {}).copy()
            
            # Merge current environment variables
            current_env = os.environ.copy()
            current_env.update(env)

            # Resolve command path if necessary
            if not os.path.isabs(command):
                resolved_command = shutil.which(command)
                if resolved_command:
                    command = resolved_command
            
            server_params = StdioServerParameters(
                command=command,
                args=args,
                env=current_env
            )

            try:
                # Create the transport and client session
                # We use the exit_stack to manage the context managers (transport and session)
                read_stream, write_stream = await self.exit_stack.enter_async_context(
                    stdio_client(server_params)
                )
                session = await self.exit_stack.enter_async_context(
                    ClientSession(read_stream, write_stream)
                )
                await session.initialize()
                
                self.sessions[name] = session
                print(f"Connected to MCP server: {name}")
                
            except Exception as e:
                print(f"Failed to connect to MCP server {name}: {e}")

    async def list_tools(self) -> Dict[str, List[Any]]:
        all_tools = {}
        for name, session in self.sessions.items():
            try:
                result = await session.list_tools()
                all_tools[name] = result.tools
            except Exception as e:
                print(f"Error listing tools for {name}: {e}")
        return all_tools

    async def call_tool(self, server_name: str, tool_name: str, arguments: Dict[str, Any] = None):
        if server_name not in self.sessions:
            raise ValueError(f"Server {server_name} not connected")
        
        session = self.sessions[server_name]
        return await session.call_tool(tool_name, arguments or {})

    async def cleanup(self):
        await self.exit_stack.aclose()
