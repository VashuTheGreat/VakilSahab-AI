import logging
from src.VakilSahab_feature.components.Google_results import Google_Search

class SearchPipeline:
    def __init__(self):
        self.google_search = Google_Search()

    async def run(self, query: str, max_results: int = 5):
        try:
            logging.info(f"Starting search pipeline for query: {query}")
            results = await self.google_search.initiate_google_search(query, max_results)
            logging.info("Search pipeline completed")
            return results
        except Exception as e:
            logging.error(f"Error in SearchPipeline: {e}")
            raise e
