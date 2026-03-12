
from src.VakilSahab_feature.constants import DOWNLOAD_DATA_CONFIG_PATH
from src.VakilSahab_feature.entity.config_entity import DATA_INGESTION_CONFIG
from utils.main_utils import read_yaml_file_sync
from utils.asyncHandler import asyncHandler
from src.VakilSahab_feature.data_access.connect_kaggle import ConnectKaggle
from src.VakilSahab_feature.entity.artifact_entity import DATA_INGESTION_ARTIFACT
import logging

class Data_Ingestor:
    def __init__(self,data_ingestion_config:DATA_INGESTION_CONFIG):
        self._schema=read_yaml_file_sync(data_ingestion_config.download_Data_config_path)
        self.data_ingestion_config=data_ingestion_config

    @asyncHandler
    async def initiate_data_ingestion(self)->DATA_INGESTION_ARTIFACT:
        logging.info("Initiating data ingestion")
        connect_kaggle=ConnectKaggle()
        logging.info("Downloading data")
        download_links=self._schema['KAGGLE_DATA_URLS']
        for link in download_links:
            logging.info(f"Downloading data from {link}")
            await connect_kaggle.download_data(link,self.data_ingestion_config.downloaded_Data_folder)

        data_ingestion_artifact = DATA_INGESTION_ARTIFACT(downloaded_data_path=self.data_ingestion_config.downloaded_Data_folder)  
        logging.info("Data ingestion completed")
        return data_ingestion_artifact

        


