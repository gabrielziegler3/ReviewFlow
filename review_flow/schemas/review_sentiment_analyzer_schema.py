from pydantic import BaseModel


class SentimentRequest(BaseModel):
    texts: list[str]


class SentimentResponse(BaseModel):
    sentiment: str
    confidence: float
