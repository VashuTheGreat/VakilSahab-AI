


from langchain_mcp_adapters.client import MultiServerMCPClient

from src.MCP_Client.contants import TRANSPORT_TYPE,MCP_SERVER_URL
class MCP_tool:
    def __init__(self):
        self.client=MultiServerMCPClient({
        "remote_server": {
            "transport":TRANSPORT_TYPE ,  # Or "streamable_http"
            "url": MCP_SERVER_URL ,  # Your port here
            # Optional: "headers": {"Authorization": "Bearer token"}
        }
    })
    
    async def get_tools(self):
        return await self.client.get_tools()
    
    

