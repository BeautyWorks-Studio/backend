from flask import request, jsonify
from app.models.product import Product
from app.config.cloudinary_config import cloudinary

def add_product():
    try:
        data = request.form
        images = request.files.getlist("images")
        image_urls = []

        for img in images:
            upload_result = cloudinary.uploader.upload(img)
            image_urls.append(upload_result["secure_url"])

        product = Product(
            name=data.get("name"),
            description=data.get("description"),
            price=float(data.get("price")),
            category=data.get("category"),
            sub_category=data.get("subCategory"),
            sizes=data.get("sizes").split(","),
            bestseller=data.get("bestseller") == "true",
            image_urls=image_urls
        ).save()

        return jsonify({"success": True, "message": "Product added", "id": str(product.id)})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 400

def list_products():
    products = Product.objects()
    return jsonify({"success": True, "products": [p.to_mongo().to_dict() for p in products]})

def get_product():
    data = request.get_json()
    product_id = data.get("productId")
    product = Product.objects(id=product_id).first()
    if not product:
        return jsonify({"success": False, "message": "Product not found"}), 404
    return jsonify({"success": True, "product": product.to_mongo().to_dict()})

def delete_product():
    data = request.get_json()
    product_id = data.get("id")
    Product.objects(id=product_id).delete()
    return jsonify({"success": True, "message": "Product deleted"})
