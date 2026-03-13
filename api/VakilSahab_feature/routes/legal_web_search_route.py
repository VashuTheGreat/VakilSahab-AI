import fastapi
from api.VakilSahab_feature.services.search_service import legal_search_logic
import logging
router=fastapi.APIRouter()

@router.get("/legal_web_search", operation_id="legal_web_search")
async def legal_web_search(query: str, max_results: int = 5):
    """
    Search the web for legal information.
    """
    return await legal_search_logic(query, max_results)
