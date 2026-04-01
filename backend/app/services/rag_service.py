from app.services.product_service import (
    get_product_by_keyword,
    get_specs,
    get_features,
    get_promotions
)

from app.services.nlp_service import normalize_text


# 🧠 Detect intent
def detect_intent(question: str):
    q = question.lower()

    if "giá" in q:
        return "price"

    if "khuyến mãi" in q:
        return "promo"

    if "thông số" in q or "bao nhiêu chế độ" in q:
        return "spec"

    if "tính năng" in q or "có gì" in q:
        return "feature"

    return "all"


# 🔥 Build context theo intent
def build_context(product, specs, features, promos, intent):
    spec_text = "\n".join([f"{k}: {v}" for k, v in specs.items()])
    feature_text = "\n".join([f"- {f}" for f in features])
    promo_text = "\n".join([f"- {p}" for p in promos])

    if intent == "price":
        return f"Giá: {product.price} VNĐ (Giảm {product.discount_percent}%)"

    if intent == "promo":
        return f"Khuyến mãi:\n{promo_text}"

    if intent == "spec":
        return f"Thông số:\n{spec_text}"

    if intent == "feature":
        return f"Tính năng:\n{feature_text}"

    return f"""
Tên: {product.name}
Giá: {product.price} VNĐ (Giảm {product.discount_percent}%)

Thông số:
{spec_text}

Tính năng:
{feature_text}

Khuyến mãi:
{promo_text}
"""


# 🚀 MAIN FUNCTION
def get_rag_context(db, question: str):
    # normalize tiếng Việt
    question = normalize_text(question)

    product = get_product_by_keyword(db, question)

    print("DEBUG PRODUCT:", product)

    if not product:
        return "", "all"

    specs = get_specs(db, product.id)
    features = get_features(db, product.id)
    promos = get_promotions(db, product.id)

    intent = detect_intent(question)

    context = build_context(product, specs, features, promos, intent)

    print("DEBUG CONTEXT:\n", context)

    return context, intent