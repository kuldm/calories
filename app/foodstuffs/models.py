from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


# Модель продуктов питания
class FoodStuff(Base):
    __tablename__ = 'foodstuffs'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
