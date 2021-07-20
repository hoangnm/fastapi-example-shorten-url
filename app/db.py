from dataclasses import dataclass, field
import sqlalchemy
from sqlalchemy import Table, Integer, Column, String
from sqlalchemy.orm import registry, sessionmaker
import hashlib

from .config import settings

mapper_registry = registry()

shorten_url_table = Table(
    'shorten_url',
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('origin_url', String()),
    Column('generated_url', String(32)),
)

@dataclass
class ShortenUrl:
    id: int = field(init=False)
    origin_url: str
    generated_url: str = field(init=False)

    def __post_init__(self):
        self.generated_url = hashlib.md5(self.origin_url.encode()).hexdigest()


mapper_registry.map_imperatively(ShortenUrl, shorten_url_table)

engine = sqlalchemy.create_engine(settings.db_url)
mapper_registry.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
