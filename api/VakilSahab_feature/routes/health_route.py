import fastapi
from fastapi.responses import JSONResponse
router=fastapi.APIRouter()
import logging

@router.get("/health")
async def health():
    """
    Check the health of the VakilSahab-AI API.
    """
    return JSONResponse(status_code=200,content={"message": "VakilSahab-AI API is running"})