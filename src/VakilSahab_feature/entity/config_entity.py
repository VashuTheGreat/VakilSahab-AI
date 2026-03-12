from src.VakilSahab_feature.constants import DOWNLOAD_DATA_CONFIG_PATH
from dataclasses import dataclass
from src.VakilSahab_feature.constants import *
import os
from datetime import datetime
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")


@dataclass
class DATA_INGESTION_CONFIG:
    download_Data_config_path:str=DOWNLOAD_DATA_CONFIG_PATH
    downloaded_Data_folder:str=DOWNLOADED_DATA_FOLDER
    
