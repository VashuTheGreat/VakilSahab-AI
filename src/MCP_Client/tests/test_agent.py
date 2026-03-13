import os
import sys
import asyncio
sys.path.append(os.getcwd())
from logger import *
from dotenv import load_dotenv
load_dotenv()

from src.MCP_Client.graphs.builder import agent

if __name__ == "__main__":
    from langchain_core.messages import HumanMessage
    async def main():
        res = await agent.ainvoke({"messages": [HumanMessage(content="Hello, how are you?")]})
        print(res)
        print(res["messages"][-1].content)
    
    asyncio.run(main())