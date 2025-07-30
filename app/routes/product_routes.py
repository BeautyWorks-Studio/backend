from flask import Blueprint, request, jsonify
from app.middleware.admin_auth import admin_auth
from app.middleware.upload_middleware import handle_uploads
from app.controllers.product_controller import (
    list_products, add_product, remove_product, single_product
)

product_bp = Blueprint('product', __name__, url_prefix='/api/products')

@product_bp.route('/add', methods=['POST'])
@admin_auth
@handle_uploads(['image1', 'image2', 'image3', 'image4'])
def add_product_route():
    return add_product(request)

@product_bp.route('/remove', methods=['POST'])
@admin_auth
def remove_product_route():
    return remove_product(request)

@product_bp.route('/single', methods=['POST'])
def single_product_route():
    return single_product(request)

@product_bp.route('/list', methods=['GET'])
def list_products_route():
    return list_products()
