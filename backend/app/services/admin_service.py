from app.models.user import User
from app.models.message import Message
from app.models.conversation import Conversation

def get_all_users(db):
    return db.query(User).all()

def get_user_messages(db, user_id):
    convo = db.query(Conversation).filter_by(user_id=user_id).first()
    if not convo:
        return []
    return db.query(Message).filter_by(conversation_id=convo.id).all()