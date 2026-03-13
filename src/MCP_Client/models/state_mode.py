from pydantic import BaseModel
from typing import Annotated
from langchain_core.messages import BaseMessage
import operator

class State(BaseModel):
    messages: Annotated[list[BaseMessage], operator.add]
