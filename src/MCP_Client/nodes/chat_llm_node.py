from utils.asyncHandler import asyncHandler
from src.MCP_Client.models.state_mode import State
from src.MCP_Client.llm.llm_loader import llm
from src.MCP_Client.tools.mcp_as_a_tool import MCP_tool
import logging

@asyncHandler
async def chat_llm(state: State):
    logging.info("Entered in chat_llm node")
    mcp = MCP_tool()
    mcp_tools = await mcp.get_tools()
    llm_with_mcp_tools = llm.bind_tools(mcp_tools)
    
    # Use the message history from state
    res = await llm_with_mcp_tools.ainvoke(state.messages)
    
    return {"messages": [res]}

