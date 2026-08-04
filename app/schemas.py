from pydantic import BaseModel
from typing import List


class EndpointRequest(BaseModel):
    endpoints: List[str]