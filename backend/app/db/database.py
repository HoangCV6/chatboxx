from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DB_URL

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()  # 👈 PHẢI CÓ DÒNG NÀY

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()