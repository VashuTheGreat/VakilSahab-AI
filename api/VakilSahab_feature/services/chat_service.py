from api.utils.main_utils import get_pipeline
import logging

async def ask_vakil_logic(question: str, docs_path: str = "data", db_path: str = "db", k: int = 5):
    """
    Logic for the VakilSahab legal assistant.
    """
    try:
        logging.info(f"Service: ask_vakil_logic called with question: {question}")
        pipeline = get_pipeline('chat')
        response = await pipeline.run(question, docs_path, db_path, k)
        return str(response)
    except Exception as e:
        logging.error(f"Error in ask_vakil_logic: {e}")
        return f"Error in legal assistant: {str(e)}"
