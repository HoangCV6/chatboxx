from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.chat_schema import ChatRequest
from app.db.database import get_db
from app.services.chat_service import get_or_create_conversation, save_message
from app.services.deepseek_service import ask_deepseek
from app.services.rag_service import get_rag_context

router = APIRouter(prefix="/chat")

@router.post("/")
def chat(req: ChatRequest, db: Session = Depends(get_db)):
    convo = get_or_create_conversation(db, req.user_id)

    save_message(db, convo.id, "user", req.message)

    # 🔥 lấy context + intent
    context, intent = get_rag_context(db, req.message)

    messages = [
        {
            "role": "system",
            "content": """
Bạn là chatbot tư vấn sản phẩm nội bộ.

QUY TẮC:
- CHỈ trả lời dựa trên dữ liệu được cung cấp
- KHÔNG được bịa
- Nếu không có dữ liệu → nói: "Tôi chưa có thông tin"
- Trả lời NGẮN GỌN
- Ưu tiên bullet points
"""
        },
        {
            "role": "user",
            "content": f"""
DỮ LIỆU:
{context}

CÂU HỎI:
{req.message}

TRẢ LỜI:
"""
        }
    ]

    reply = ask_deepseek(messages)

    save_message(db, convo.id, "bot", reply)

    return {"reply": reply}