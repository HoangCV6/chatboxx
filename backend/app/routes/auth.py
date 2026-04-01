from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate
from app.models.user import User
from app.db.database import get_db

router = APIRouter(prefix="/auth")

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, phone=user.phone, role="user")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user