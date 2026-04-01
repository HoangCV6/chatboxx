import requests
from app.config import DEEPSEEK_API_KEY

def ask_deepseek(messages):
    url = "https://api.deepseek.com/chat/completions"

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek-chat",
        "messages": messages
    }

    response = requests.post(url, json=payload, headers=headers)

    # 👇 IN RA DEBUG
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    data = response.json()

    # 👇 CHECK LỖI
    if "choices" not in data:
        return f"Lỗi API: {data}"

    return data["choices"][0]["message"]["content"]