from codecs import ignore_errors
import os
import json
import opendatasets as od

from src.VakilSahab_feature.constants import DATA_DIR
from utils.asyncHandler import asyncHandler
from src.VakilSahab_feature.constants import USERNAME,KAGGLE_KEY,KAGGLE_CRED_FILE

class ConnectKaggle:
    def __init__(self):
        self.od=od
        self._setup_credentials()

    def _setup_credentials(self):
        """Ensures Kaggle credentials are available for opendatasets without triggering prompts."""
       
        
        if USERNAME and KAGGLE_KEY:
            cred_file = KAGGLE_CRED_FILE
            if not os.path.exists(cred_file):
                with open(cred_file, "w") as f:
                    json.dump({"username": USERNAME, "key": KAGGLE_KEY}, f)
                    
        
    @asyncHandler
    async def download_data(self,url:str,data_dir:str=DATA_DIR):
        self.od.download(dataset_id_or_url=url,data_dir=data_dir)    



