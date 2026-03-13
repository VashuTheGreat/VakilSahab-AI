import fastapi
from src.MCP_Client.pipelines.mcp_agent_pipeline import MCP_Agent_Pipeline
from fastapi.responses import JSONResponse
import json
router=fastapi.APIRouter()
mcp_agent_pipeline=MCP_Agent_Pipeline()


@router.post("/chat_agent")
async def chat_agent(query:str="What are the most important human rights"):
    try:
        response = await mcp_agent_pipeline.ainvoke(query)
        
        reply = "I'm sorry, I couldn't understand the response."
        if hasattr(response, "get"):
            messages = response.get("messages", [])
            if messages:
                last_msg = messages[-1]
                if hasattr(last_msg, 'content'):
                    reply = last_msg.content
                elif isinstance(last_msg, dict) and 'content' in last_msg:
                    reply = last_msg['content']
                    
        return {"data": reply}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
