
from src.MCP_Client.graphs.builder import agent
from langchain_core.messages import HumanMessage

class MCP_Agent_Pipeline:
    def __init__(self):
        self.agent = agent
    
    
    
    async def ainvoke(self, messages:str):
        return await self.agent.ainvoke({"messages": [HumanMessage(content=messages)]})