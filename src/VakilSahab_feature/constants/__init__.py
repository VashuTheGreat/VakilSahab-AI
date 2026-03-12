
import os
DATA_DIR="data"

DOWNLOAD_DATA_CONFIG_PATH=os.path.join("src","VakilSahab_feature","configurations","download_data_config.yaml")

DOWNLOADED_DATA_FOLDER=os.path.join("data")


# ------------ Kaggle Tokens -----------------
USERNAME=os.getenv("KAGGLE_USERNAME")
KAGGLE_KEY=os.getenv("KAGGLE_KEY")
KAGGLE_CRED_FILE=os.path.join("kaggle.json")





# ---------- RAG LLM --------------------

EMBEDDING_MODEL="sentence-transformers/all-MiniLM-L6-v2"

EXCEPTED_FILE_TYPE=['txt','pdf','http']

RETREIVER_DEFAULT_K=3

LOGS_DIR="logs"
LLM_MODEL_ID = "us.meta.llama3-3-70b-instruct-v1:0"
LLM_REGION = "us-east-1"


TOP_K_KEYWORDS=10

CONTENT_PERSISTENT_TIME=60 # 5 MIN
DATA_FOLDER_PATH="data"
DB_FOLDER_PATH="db"


