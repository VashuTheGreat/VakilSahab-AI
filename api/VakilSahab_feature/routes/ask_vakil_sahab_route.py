import fastapi
from api.VakilSahab_feature.services.chat_service import ask_vakil_logic
router=fastapi.APIRouter()
import logging

@router.post("/ask_vakil_sahab", operation_id="ask_vakil_sahab")
async def ask_vakil_sahab(user_query: str, docs_path: str = "data", db_path: str = "db", k: int = 5):
    """
    Ask Vakil Sahab - Ask questions about Indian law and get answers with citations.
    """
    return await ask_vakil_logic(user_query, docs_path, db_path, k)
