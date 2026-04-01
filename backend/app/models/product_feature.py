from sqlalchemy import Column, Integer, ForeignKey, String, Text
from app.db.database import Base

class ProductFeature(Base):
    __tablename__ = "product_features"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    title = Column(String(255))
    content = Column(Text)