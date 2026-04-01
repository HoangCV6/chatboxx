from pydantic import BaseModel

class ChatRequest(BaseModel):
    user_id: int
    message: str

class AdminReply(BaseModel):
    user_id: int
    message: str