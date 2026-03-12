
import os
DATA_DIR="data"

DOWNLOAD_DATA_CONFIG_PATH=os.path.join("src","VakilSahab_feature","configurations","download_data_config.yaml")

DOWNLOADED_DATA_FOLDER=os.path.join("data")


# ------------ Kaggle Tokens -----------------
USERNAME=os.getenv("KAGGLE_USERNAME")
KAGGLE_KEY=os.getenv("KAGGLE_KEY")
KAGGLE_CRED_FILE=os.path.join("kaggle.json")