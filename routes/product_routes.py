from flask import Blueprint, request, jsonify
from app.models.product import Product
from app import db

product_bp = Blueprint('product_bp', __name__, url_prefix='/products')

# Create a new product
@product_bp.route('/', methods=['POST'])
def create_product():
    data = request.get_json()

    try:
        new_product = Product(
            name=data['name'],
            price=data['price'],
            image=data.get('image'),
            stock=data.get('stock', 0)
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Read all products
@product_bp.route('/', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200


# Read one product by ID
@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify(product.to_dict()), 200
    return jsonify({'error': 'Product not found'}), 404


# Update a product
@product_bp.route('/<int:product_id>', methods=['PATCH'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    data = request.get_json()
    product.name = data.get('name', product.name)
    product.price = data.get('price', product.price)
    product.image = data.get('image', product.image)
    product.stock = data.get('stock', product.stock)

    db.session.commit()
    return jsonify(product.to_dict()), 200


# Delete a product
@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 200
