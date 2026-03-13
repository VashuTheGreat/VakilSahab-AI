import logging
from src.VakilSahab_feature.graphs.builder import graph

class ChatPipeline:
    def __init__(self):
        self.graph = graph

    async def run(self, user_query: str, docs_path: str = "data", db_path: str = "db", k: int = 5):
        try:
            logging.info(f"Starting chat pipeline for query: {user_query}")
            res = await self.graph.ainvoke({
                "userQuery": user_query,
                "docs_path": docs_path,
                "db_path": db_path,
                "k": k
            })
            logging.info("Chat pipeline completed")
            return res['messages'][-1].content
        except Exception as e:
            logging.error(f"Error in ChatPipeline: {e}")
            raise e
