# Lazy initialization to avoid circular imports
_pipeline_factories = {
    'ingestion': lambda: __import__('src.VakilSahab_feature.pipelines.ingestion_pipeline', fromlist=['IngestionPipeline']).IngestionPipeline(),
    'search': lambda: __import__('src.VakilSahab_feature.pipelines.search_pipeline', fromlist=['SearchPipeline']).SearchPipeline(),
    'chat': lambda: __import__('src.VakilSahab_feature.pipelines.chat_pipeline', fromlist=['ChatPipeline']).ChatPipeline()
}

_pipeline_instances = {}

def get_pipeline(name):
    if name not in _pipeline_instances:
        if name in _pipeline_factories:
            _pipeline_instances[name] = _pipeline_factories[name]()
        else:
            raise ValueError(f"Unknown pipeline: {name}")
    return _pipeline_instances[name]
