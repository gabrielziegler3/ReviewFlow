from pydantic import BaseModel


class ReviewCreate(BaseModel):
    text: str
    sentiment: str


class ReviewResponse(BaseModel):
    id: int
    text: str
    sentiment: str

    class Config:
        from_attributes = True  # Allows ORM compatibility
