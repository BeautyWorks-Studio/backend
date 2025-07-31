from flask import Blueprint
from app.controllers.product_controller import (
    add_product,
    list_products,
    get_product,
    delete_product
)

product_bp = Blueprint("product_bp", __name__)

product_bp.route("/", methods=["POST"])(add_product)
product_bp.route("/", methods=["GET"])(list_products)
product_bp.route("/<product_id>", methods=["GET"])(get_product)
product_bp.route("/delete", methods=["POST"])(delete_product)
