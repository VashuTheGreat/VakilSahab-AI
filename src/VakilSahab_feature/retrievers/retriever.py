import logging
from utils.asyncHandler import asyncHandler
from src.VakilSahab_feature.constants import EXCEPTED_FILE_TYPE,RETREIVER_DEFAULT_K
from src.VakilSahab_feature.utils.ingestion_utils import create_vector_store
from src.VakilSahab_feature.entity.config_entity import RAG_IngestionConfig
import os

from src.VakilSahab_feature.utils.ingestion_utils import create_retreiver


class Retreiver:
    def __init__(self,vector_db,k:int=RETREIVER_DEFAULT_K):
        self.vector_db=vector_db
        self.k=k
        self.retreiver=None
        

    @asyncHandler
    async def initiate_retreiver(self):
        logging.info("Initiating retriever...")
        retreiver = await create_retreiver(vectorstore=self.vector_db, k=self.k)
        self.retreiver = retreiver
        logging.info("Retriever initiated successfully.")

    @asyncHandler
    async def invoke(self, query: str = "ML algorithms train on datasets"):
        logging.info(f"Invoking retriever with query: {query}")
        result = self.retreiver.invoke(query)
        logging.info("Retriever invocation successful.")
        return result