from dataclasses import dataclass
from typing import Any
from src.VakilSahab_feature.constants import RETREIVER_DEFAULT_K

@dataclass
class DATA_INGESTION_ARTIFACT:
    downloaded_data_path:str


@dataclass
class RAG_IngestionArtifact:
    vector_db:Any    