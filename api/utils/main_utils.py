from src.VakilSahab_feature.pipelines.ingestion_pipeline import IngestionPipeline
from src.VakilSahab_feature.pipelines.search_pipeline import SearchPipeline
from src.VakilSahab_feature.pipelines.chat_pipeline import ChatPipeline


_pipelines = {
    "ingestion": None,
    "search": None,
    "chat": None
}

_pipelines['ingestion']=IngestionPipeline()
_pipelines["search"] = SearchPipeline()
_pipelines["chat"] = ChatPipeline()
