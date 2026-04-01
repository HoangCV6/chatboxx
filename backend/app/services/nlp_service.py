def normalize_text(text: str):
    text = text.lower()

    mapping = {
        "ghế": "",
        "massage": "",
        "giá bao nhiêu": "giá",
        "bao nhiêu tiền": "giá",
        "chế độ": "program",
        "bài massage": "program",
        "nóng": "nhiệt",
        "sưởi": "nhiệt"
    }

    for k, v in mapping.items():
        text = text.replace(k, v)

    return text.strip()