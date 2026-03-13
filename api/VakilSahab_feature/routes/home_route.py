import fastapi
import logging

router=fastapi.APIRouter()


@router.get("/")
async def home():
    """
    Check the health of the VakilSahab-AI API.
    """
    return {"message": "VakilSahab-AI API is running"}