from sqlalchemy import Column, Integer, ForeignKey, Text, Enum, DateTime
from datetime import datetime
from app.db.database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    sender = Column(Enum("user", "bot", "admin"))
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)