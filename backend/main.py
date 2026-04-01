# backend/main.py
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

# Import routers - đường dẫn đúng với cấu trúc của bạn
from app.routes import auth, chat, admin, product

# Tạo app
app = FastAPI(title="Chatbot API", version="1.0.0")

# CORS - cấu hình cụ thể hơn cho production
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",      # React dev
        "http://localhost:5173",      # Vite dev
        "https://your-frontend.vercel.app",  # Thay sau khi deploy frontend
        "https://chatboxx.vercel.app",       # URL frontend thực tế
        "*"  # Tạm thời cho phép tất cả (chỉ dùng khi test)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])
app.include_router(product.router, prefix="/api/products", tags=["products"])

# WebSocket connections
connections = {}

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await websocket.accept()
    connections[user_id] = websocket
    try:
        while True:
            data = await websocket.receive_text()
            # Xử lý message với DeepSeek API ở đây
            await websocket.send_text(f"Echo: {data}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        del connections[user_id]

# Health check endpoint
@app.get("/")
async def root():
    return {"message": "Chatbot API is running", "status": "healthy"}

@app.get("/api/health")
async def health():
    return {"status": "ok", "message": "Backend is ready"}

# Chạy uvicorn (chỉ dùng khi chạy local)
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)