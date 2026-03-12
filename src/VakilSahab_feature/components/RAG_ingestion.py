import logging
from utils.asyncHandler import asyncHandler
from src.VakilSahab_feature.constants import EXCEPTED_FILE_TYPE
from src.VakilSahab_feature.utils.ingestion_utils import create_vector_store
from src.VakilSahab_feature.entity.config_entity import RAG_IngestionConfig
from src.VakilSahab_feature.entity.artifact_entity import RAG_IngestionArtifact
import os

class RAG_Ingestion:
    def __init__(self,ingestion_config:RAG_IngestionConfig):
        self.ingestion_config=ingestion_config
    @asyncHandler
    async def ingest_data(self):
        logging.info(f"Starting data ingestion... DB path: {self.ingestion_config.db_path}, Docs path: {self.ingestion_config.docs_path}")
        vector_db = await create_vector_store(path=self.ingestion_config.db_path, docs=self.ingestion_config.docs_path)
        logging.info("Vector store loaded/created successfully.")
        ingestion_artifact=RAG_IngestionArtifact(vector_db=vector_db)
        return ingestion_artifact
        

