from pydantic import BaseModel

class CreateShortenUrlPayload(BaseModel):
    url: str

class ShortenUrlResponse(BaseModel):
    id: int
    origin_url: str
    generated_url: str

    class Config:
        orm_mode = True
