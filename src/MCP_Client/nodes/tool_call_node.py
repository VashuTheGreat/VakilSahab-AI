from utils.asyncHandler import asyncHandler
from src.MCP_Client.models.state_mode import State
from langchain_core.messages import ToolMessage
from src.MCP_Client.tools.mcp_as_a_tool import MCP_tool
import logging

@asyncHandler
async def tool_call(state: State):
    logging.info("Entered in tool_call node")
    mcp = MCP_tool()
    mcp_tools = await mcp.get_tools()
    tools_by_name = {tool.name: tool for tool in mcp_tools}
    
    results = []
    last_message = state.messages[-1]
    
    if hasattr(last_message, 'tool_calls'):
        for t_call in last_message.tool_calls:
            tool = tools_by_name[t_call['name']]
            observation = await tool.ainvoke(t_call['args'])
            results.append(ToolMessage(content=str(observation), tool_call_id=t_call['id']))
            
    return {"messages": results}

