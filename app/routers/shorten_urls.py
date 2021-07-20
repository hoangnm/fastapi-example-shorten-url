from typing import List
from fastapi import status, APIRouter
from app.schemas import CreateShortenUrlPayload, ShortenUrlResponse
from app.handlers import shorten_urls_handler as handlers

router = APIRouter(
    prefix="/shorten_urls",
    tags=["urls"],
)

@router.get("", response_model=List[ShortenUrlResponse])
def get_shorten_urls():
    return handlers.get_shorten_urls()

@router.post("", response_model=ShortenUrlResponse, status_code=status.HTTP_201_CREATED)
def create_shorten_url(payload: CreateShortenUrlPayload):
    url = handlers.create_shorten_url(payload)
    return url
