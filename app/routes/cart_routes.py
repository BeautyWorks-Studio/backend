from flask import Blueprint, request
from app.middleware.auth import auth_user
from app.controller.cart_controller import get_user_cart, add_to_cart, update_cart

cart_bp = Blueprint('cart', __name__, url_prefix='/api/cart')

@cart_bp.route('/get', methods=['POST'])
@auth_user
def get_cart():
    return get_user_cart(request)

@cart_bp.route('/add', methods=['POST'])
@auth_user
def add_cart():
    return add_to_cart(request)

@cart_bp.route('/update', methods=['POST'])
@auth_user
def update_cart_route():
    return update_cart(request)

