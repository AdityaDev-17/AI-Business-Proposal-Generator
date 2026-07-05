from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    request: str = Field(
        ...,
        min_length=10,
        max_length=1000,
        description="Natural language business request",
    )