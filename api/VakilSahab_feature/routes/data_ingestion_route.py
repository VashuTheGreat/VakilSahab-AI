import fastapi

from api.utils.main_utils import _pipelines
import logging
router=fastapi.APIRouter()



@router.get("/ingest_legal_data")
async def ingest_legal_data():
    """
    Ingest legal data from the web into the local database.
    
    Returns:
        str: The path to the downloaded data.
    """
    try:
        logging.info("MCP Tool: ingest_legal_data called")
        pipeline = _pipelines['ingestion']
        artifact = await pipeline.run()
        return f"Data ingestion completed. Data located at: {artifact.downloaded_data_path}"
    except Exception as e:
        return f"Error during data ingestion: {str(e)}"