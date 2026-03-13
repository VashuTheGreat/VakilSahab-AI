from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

from api.VakilSahab_feature.routes import ask_vakil_sahab_route,data_ingestion_route,legal_web_search_route,health_route,home_route

app = FastAPI(title="VakilSahab-AI API")









app.include_router(prefix="/api/v1/chat",router=ask_vakil_sahab_route.router)
app.include_router(prefix="/api/v1/ingest",router=data_ingestion_route.router)
app.include_router(prefix="/api/v1/search",router=legal_web_search_route.router)


# ------------------ Some Routes ----------------------------------
app.include_router(prefix="",router=health_route.router)
app.include_router(prefix="",router=home_route.router)





# --------------- MCP -------------------

mcp = FastApiMCP(app)
mcp.mount_http()
