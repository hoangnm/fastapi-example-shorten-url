from app.db import SessionLocal
from app.models import ShortenUrl

def get_shorten_urls():
    db = SessionLocal()
    try:
        return db.query(ShortenUrl).all()
    finally:
        db.close()

def create_shorten_url(payload):
    db = SessionLocal()
    try:
        url = ShortenUrl(payload.url)
        db.add(url)
        db.commit()
        db.refresh(url)
        return url
    finally:
        db.close()
