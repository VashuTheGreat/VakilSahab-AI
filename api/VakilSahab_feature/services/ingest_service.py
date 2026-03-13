from api.utils.main_utils import get_pipeline
import logging

async def ingest_logic(source: str):
    """
    Logic for data ingestion.
    Note: The source argument is currently ignored as the pipeline downloads from fixed URLs,
    but it's kept for future extensibility (e.g., local files or custom URLs).
    """
    try:
        logging.info(f"Service: ingest_logic called with source: {source}")
        pipeline = get_pipeline('ingestion')
        artifact = await pipeline.run()
        return f"Data ingestion completed. Data located at: {artifact.downloaded_data_path}"
    except Exception as e:
        logging.error(f"Error in ingest_logic: {e}")
        return f"Error during data ingestion: {str(e)}"
