from app.models.message import Message
from app.models.conversation import Conversation

def get_or_create_conversation(db, user_id):
    convo = db.query(Conversation).filter_by(user_id=user_id).first()
    if not convo:
        convo = Conversation(user_id=user_id)
        db.add(convo)
        db.commit()
        db.refresh(convo)
    return convo

def save_message(db, conversation_id, sender, content):
    msg = Message(
        conversation_id=conversation_id,
        sender=sender,
        content=content
    )
    db.add(msg)
    db.commit()