from sqlalchemy import Column, Integer, ForeignKey, String, Text
from app.db.database import Base

class ProductSpec(Base):
    __tablename__ = "product_specs"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    spec_key = Column(String(100))
    spec_value = Column(Text)