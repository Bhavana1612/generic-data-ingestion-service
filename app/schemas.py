from pydantic import BaseModel
from typing import List, Dict


class APIConfig(BaseModel):
    url: str
    method: str = "GET"
    headers: Dict[str, str] = {}


class IngestionRequest(BaseModel):
    sources: List[APIConfig]