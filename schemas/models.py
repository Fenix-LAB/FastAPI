from pydantic import BaseModel, Field
from typing import List


class Fruit(BaseModel):
    name: str
    sugar: int

class FruitList(BaseModel):
    ListF: List[Fruit]
    