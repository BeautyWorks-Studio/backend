from flask import Blueprint, request, jsonify
from app.models import Product
from app import db
from flask_jwt_extended import jwt_required
from app.utils.decorators import role_required

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "price": p.price,
        "image": p.image,
        "stock": p.stock
    } for p in products])

@product_bp.route('/', methods=['POST'])
@jwt_required()
@role_required(['admin', 'staff'])
def create_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        price=data['price'],
        image=data.get('image', ''),
        stock=data.get('stock', 0)
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"msg": "Product added"}), 201

@product_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
@role_required(['admin', 'staff'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    product.name = data['name']
    product.price = data['price']
    product.image = data.get('image', product.image)
    product.stock = data.get('stock', product.stock)
    db.session.commit()
    return jsonify({"msg": "Product updated"})

@product_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
@role_required(['admin', 'staff'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"msg": "Product deleted"})
