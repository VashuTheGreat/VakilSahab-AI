import asyncio
import os
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_mcp_server():
    # Configure the server parameters
    # We use 'uv run' to ensure the correct environment and dependencies
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "api/mcp_server.py"],
        env=os.environ.copy()
    )

    print("--- Connecting to MCP Server ---")
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()

            # List available tools
            print("\n--- Available Tools ---")
            tools_result = await session.list_tools()
            for tool in tools_result.tools:
                print(f"- {tool.name}: {tool.description}")

            # Test a simple tool: legal_web_search
            print("\n--- Testing legal_web_search ---")
            search_res = await session.call_tool("legal_web_search", {"query": "Latest Indian Supreme Court judgements 2024", "max_results": 2})
            print(f"Search Results: {search_res.content[0].text[:500]}...")

            # Note: ingesting data or full chat might be slow for a quick test
            # print("\n--- Testing ask_vakil_sahab ---")
            # chat_res = await session.call_tool("ask_vakil_sahab", {"user_query": "What is IPC section 302?"})
            # print(f"Chat Results: {chat_res.content[0].text}")

if __name__ == "__main__":
    try:
        asyncio.run(test_mcp_server())
    except Exception as e:
        print(f"\nError: {e}")
