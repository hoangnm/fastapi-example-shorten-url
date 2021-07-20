from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.db import ShortenUrl, SessionLocal

app = FastAPI(title="Shorten url service")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class CreateShortenUrlPayload(BaseModel):
    url: str

class ShortenUrlResponse(BaseModel):
    id: int
    origin_url: str
    generated_url: str

    class Config:
        orm_mode = True

def handle_create_shorten_url(payload: CreateShortenUrlPayload, db: Session):
    url = ShortenUrl(payload.url)
    db.add(url)
    db.commit()
    return url

@app.get("/shorten_urls", response_model=List[ShortenUrlResponse])
def get_shorten_urls(db: Session = Depends(get_db)):
    return db.query(ShortenUrl).all()

@app.post("/shorten_urls", response_model=ShortenUrlResponse)
def create_shorten_url(payload: CreateShortenUrlPayload, db: Session = Depends(get_db)):
    url = handle_create_shorten_url(payload, db)
    return url
