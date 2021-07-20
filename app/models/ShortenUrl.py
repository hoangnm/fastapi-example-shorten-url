from dataclasses import dataclass, field
import hashlib

@dataclass
class ShortenUrl:
    id: int = field(init=False)
    origin_url: str
    generated_url: str = field(init=False)

    def __post_init__(self):
        self.generated_url = hashlib.md5(self.origin_url.encode()).hexdigest()

