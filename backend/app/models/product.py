from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.db.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    category = Column(String(100))
    price = Column(Integer)
    original_price = Column(Integer)
    discount_percent = Column(Integer)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)