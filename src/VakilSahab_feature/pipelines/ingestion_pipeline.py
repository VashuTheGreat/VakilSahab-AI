import logging
from src.VakilSahab_feature.entity.config_entity import DATA_INGESTION_CONFIG
from src.VakilSahab_feature.components.Data_ingestion import Data_Ingestor
from src.VakilSahab_feature.entity.artifact_entity import DATA_INGESTION_ARTIFACT

class IngestionPipeline:
    def __init__(self):
        self.data_ingestion_config = DATA_INGESTION_CONFIG()
        self.data_ingestion = Data_Ingestor(self.data_ingestion_config)

    async def run(self) -> DATA_INGESTION_ARTIFACT:
        try:
            logging.info("Starting ingestion pipeline")
            artifact = await self.data_ingestion.initiate_data_ingestion()
            logging.info("Ingestion pipeline completed")
            return artifact
        except Exception as e:
            logging.error(f"Error in IngestionPipeline: {e}")
            raise e
