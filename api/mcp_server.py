from fastapi import FastAPI, Request
from fastapi_mcp import FastApiMCP
import logging

from api.VakilSahab_feature.routes import (
    ask_vakil_sahab_route,
    data_ingestion_route,
    legal_web_search_route,
    health_route,
    home_route
)

from api.MCP_client.routes import chat_agent_route

app = FastAPI(title="VakilSahab-AI API")


# ---------------- REST API ----------------

app.include_router(prefix="/api/v1/chat", router=ask_vakil_sahab_route.router)
app.include_router(prefix="/api/v1/ingest", router=data_ingestion_route.router)
app.include_router(prefix="/api/v1/search", router=legal_web_search_route.router)
app.include_router(prefix="/api/v1/chat_mcp_agent", router=chat_agent_route.router)

app.include_router(prefix="", router=health_route.router)
app.include_router(prefix="", router=home_route.router)


# ---------------- MCP Server ----------------
mcp = FastApiMCP(app,include_operations=["ask_vakil_sahab","legal_web_search"])

mcp.mount_http()


