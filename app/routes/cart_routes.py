from flask import Blueprint
from app.controller.cart_controller import get_cart, add_to_cart, update_cart

cart_bp = Blueprint("cart_bp", __name__)

cart_bp.route("/", methods=["GET"])(get_cart)

cart_bp.route("/", methods=["POST"])(add_to_cart)

cart_bp.route("/", methods=["PATCH"])(update_cart)

