from pydantic import BaseModel, Field
from typing import List


class Fruit(BaseModel):
    id: int = Field(default=0)
    name: str
    sugar: int

class FruitList(BaseModel):
    ListF: List[Fruit]
    