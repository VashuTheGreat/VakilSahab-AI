

import sys
import os
sys.path.append(os.getcwd())
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from  src.MCP_Client.llm.llm_loader import llm


async def main():
    client = MultiServerMCPClient({
        "remote_server": {
            "transport": "http",  # Or "streamable_http"
            "url": "http://localhost:8000/mcp",  # Your port here
            # Optional: "headers": {"Authorization": "Bearer token"}
        }
    })
    tools = await client.get_tools()
    print(tools)
    agent = create_react_agent(llm, tools)
    
    result = await agent.ainvoke({"messages": [("user", "Use a tool from the server")]})
    print(result)
asyncio.run(main())
