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
        print(response)
        return {"data": response}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
        
