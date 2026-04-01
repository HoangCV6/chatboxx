from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.admin_service import get_all_users, get_user_messages
from app.schemas.chat_schema import AdminReply
from app.services.chat_service import get_or_create_conversation, save_message

router = APIRouter(prefix="/admin")

@router.get("/users")
def users(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/chat/{user_id}")
def chat(user_id: int, db: Session = Depends(get_db)):
    return get_user_messages(db, user_id)

@router.post("/reply")
def reply(data: AdminReply, db: Session = Depends(get_db)):
    convo = get_or_create_conversation(db, data.user_id)
    save_message(db, convo.id, "admin", data.message)
    return {"status": "sent"}