from flask import Blueprint, request, jsonify
from models import Product
from config import db
from flask_jwt_extended import jwt_required

product_bp = Blueprint("product_bp", __name__)

# CREATE
@product_bp.route("/", methods=["POST"])
@jwt_required()
def create_product():
    data = request.get_json()
    product = Product(
        name=data["name"],
        price=data["price"],
        image=data.get("image"),
        stock=data.get("stock", 0)
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product created", "product": {
        "id": product.id,
        "name": product.name,
        "price": product.price
    }}), 201

# READ
@product_bp.route("/", methods=["GET"])
def get_products():
    products = Product.query.all()
    result = [
        {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "image": p.image,
            "stock": p.stock,
            "created_at": p.created_at
        }
        for p in products
    ]
    return jsonify(result), 200

# UPDATE
@product_bp.route("/<int:id>", methods=["PATCH"])
@jwt_required()
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    product.name = data.get("name", product.name)
    product.price = data.get("price", product.price)
    product.image = data.get("image", product.image)
    product.stock = data.get("stock", product.stock)

    db.session.commit()
    return jsonify({"message": "Product updated"}), 200

# DELETE
@product_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"}), 200

