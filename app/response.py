from typing import List
from pydantic import BaseModel


class AgentResponse(BaseModel):
    status: str
    message: str

    request: str

    tasks: List[str]

    proposal: str

    document: str