from typing import List
from fastapi import FastAPI
from app.schemas import CreateShortenUrlPayload, ShortenUrlResponse
import app.handlers as handlers

app = FastAPI(title="Shorten url service")

@app.get("/shorten_urls", response_model=List[ShortenUrlResponse])
def get_shorten_urls():
    return handlers.get_shorten_urls()

@app.post("/shorten_urls", response_model=ShortenUrlResponse)
def create_shorten_url(payload: CreateShortenUrlPayload):
    url = handlers.create_shorten_url(payload)
    return url
