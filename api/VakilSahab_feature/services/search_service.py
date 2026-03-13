from api.utils.main_utils import get_pipeline
import logging

async def legal_search_logic(query: str, max_results: int = 5):
    """
    Logic for legal web search.
    """
    try:
        logging.info(f"Service: legal_search_logic called with query: {query}")
        pipeline = get_pipeline('search')
        results = await pipeline.run(query, max_results)
        return str(results)
    except Exception as e:
        logging.error(f"Error in legal_search_logic: {e}")
        return f"Error during web search: {str(e)}"
