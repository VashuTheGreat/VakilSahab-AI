import fastapi
from api.utils.main_utils import _pipelines
router=fastapi.APIRouter()
import logging

@router.post("/ask_vakil_sahab")
async def ask_vakil_sahab(user_query: str, docs_path: str = "data", db_path: str = "db", k: int = 5):
    """
    Ask Vakil Sahab - Ask questions about Indian law and get answers with citations.
    
    Args:
        user_query (str): The question to ask.
        docs_path (str): Path to the documents.
        db_path (str): Path to the database.
        k (int): Number of documents to use for retrieval.
    
    Returns:
        str: The answer to the question.
    """
    try:
        logging.info(f"MCP Tool: ask_vakil_sahab called with query: {user_query}")
        pipeline = _pipelines['chat']
        response = await pipeline.run(user_query, docs_path, db_path, k)
        return str(response)
    except Exception as e:
        return f"Error in legal assistant: {str(e)}"
