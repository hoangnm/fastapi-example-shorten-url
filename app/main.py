from fastapi import FastAPI
from app.routers import shorten_urls

app = FastAPI(title="Shorten url service")

app.include_router(shorten_urls.router)
