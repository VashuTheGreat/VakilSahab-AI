from dotenv import load_dotenv
load_dotenv()

import sys
import os

sys.path.append(os.getcwd())
from logger import *
import asyncio

from src.VakilSahab_feature.graphs.builder import graph


async def main():

    res=await graph.ainvoke({
        "userQuery": "The territory of India shall comprise tell me about this",
        "docs_path": "data",
        "db_path": "db",
        "k": 5
    })
    print(res)

asyncio.run(main())