from sqlalchemy import Column, Integer, String, Enum, DateTime
from datetime import datetime
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    phone = Column(String(20), unique=True)
    role = Column(Enum("user", "admin"))
    created_at = Column(DateTime, default=datetime.utcnow)