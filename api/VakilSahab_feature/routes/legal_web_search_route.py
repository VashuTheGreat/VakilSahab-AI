import fastapi
from api.utils.main_utils import _pipelines
import logging
router=fastapi.APIRouter()



@router.post("/legal_web_search")
async def legal_web_search(query: str, max_results: int = 5):
    """
    Search the web for legal information.
    
    Args:
        query (str): The search query.
        max_results (int): The maximum number of results to return.
    
    Returns:
        str: The search results.
    """
    try:
        logging.info(f"MCP Tool: legal_web_search called with query: {query}")
        pipeline = _pipelines['search']
        results = await pipeline.run(query, max_results)
        return str(results)
    except Exception as e:
        return f"Error during web search: {str(e)}"
