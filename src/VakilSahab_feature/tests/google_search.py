from dotenv import load_dotenv
load_dotenv()

import sys
import os

sys.path.append(os.getcwd())
from logger import *


from src.VakilSahab_feature.components.Google_results import Google_Search
import asyncio

async def main():
    google_search=Google_Search()
    results=await google_search.initiate_google_search("What is the capital of India?")
    print(results)

if __name__ == "__main__":
    asyncio.run(main())