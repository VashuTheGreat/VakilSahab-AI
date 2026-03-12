from dotenv import load_dotenv
load_dotenv()

import sys
import os

sys.path.append(os.getcwd())
from logger import *

from src.VakilSahab_feature.entity.config_entity import DATA_INGESTION_CONFIG
from src.VakilSahab_feature.components.Data_ingestion import Data_Ingestor
from src.VakilSahab_feature.entity.artifact_entity import DATA_INGESTION_ARTIFACT


import asyncio

async def main():
    logging.info("Starting data ingestion")
    data_ingestion_config = DATA_INGESTION_CONFIG()
    data_ingestion = Data_Ingestor(data_ingestion_config)
    data_ingestion_artifact = await data_ingestion.initiate_data_ingestion()
    print(data_ingestion_artifact)
    logging.info("Data ingestion completed")

asyncio.run(main())

