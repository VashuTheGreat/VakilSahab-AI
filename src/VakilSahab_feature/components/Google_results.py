import logging
from utils.asyncHandler import asyncHandler
from src.VakilSahab_feature.tools.taivily_search_tool import Taivily_search

class Google_Search:
    def __init__(self):
        self.search_tool=Taivily_search()
    @asyncHandler
    async def initiate_google_search(self,query:str,max_results:int=5):
        logging.info(f"Starting google search for query: {query}")
        results = await self.search_tool._tavily_search(query=query, max_results=max_results)
        logging.info("Google search completed.")
        return results
        

