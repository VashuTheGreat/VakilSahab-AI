import fastapi
from api.VakilSahab_feature.services.ingest_service import ingest_logic
import logging
router=fastapi.APIRouter()

@router.get("/ingest_legal_data", operation_id="ingest_legal_data")
async def ingest_legal_data(source: str = "kaggle"):
    """
    Ingest legal data from the web into the local database.
    """
    return await ingest_logic(source)