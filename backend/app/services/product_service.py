from app.models.product import Product
from app.models.product_spec import ProductSpec
from app.models.product_feature import ProductFeature
from app.models.promotion import Promotion


# 🔥 SEARCH SẢN PHẨM
def get_product_by_keyword(db, question: str):
    q = question.lower()

    products = db.query(Product).all()

    if not products:
        return None

    for p in products:
        if p.name.lower() in q:
            return p

    keywords = q.split()

    for p in products:
        if any(k in p.name.lower() for k in keywords):
            return p

    return products[0]


# ✅ Lấy thông số
def get_specs(db, product_id: int):
    specs = db.query(ProductSpec).filter(ProductSpec.product_id == product_id).all()
    return {s.spec_key: s.spec_value for s in specs}


# ✅ Lấy tính năng
def get_features(db, product_id: int):
    features = db.query(ProductFeature).filter(ProductFeature.product_id == product_id).all()
    return [f.content for f in features]


# ✅ Lấy khuyến mãi
def get_promotions(db, product_id: int):
    promos = db.query(Promotion).filter(Promotion.product_id == product_id).all()
    return [p.content for p in promos]