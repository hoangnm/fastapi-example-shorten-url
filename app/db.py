import sqlalchemy
from sqlalchemy import Table, Integer, Column, String
from sqlalchemy.orm import registry, sessionmaker
from app.models import ShortenUrl
from app.config import settings

mapper_registry = registry()

shorten_url_table = Table(
    'shorten_url',
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('origin_url', String()),
    Column('generated_url', String(32)),
)

mapper_registry.map_imperatively(ShortenUrl, shorten_url_table)

engine = sqlalchemy.create_engine(settings.db_url)
mapper_registry.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
