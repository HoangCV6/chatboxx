from sqlalchemy import Column, Integer, ForeignKey, Text
from app.db.database import Base

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    content = Column(Text)