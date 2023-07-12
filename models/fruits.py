from config.database import base
from sqlalchemy import (Column,
                        Integer,
                        String,
                        Float)

class Fruit(base):
    __tablename__ = "Fruits"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    sugar = Column(Float)