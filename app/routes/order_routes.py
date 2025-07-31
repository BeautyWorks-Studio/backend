from flask import Blueprint, request
from app.middleware.auth import auth_user
from app.middleware.admin_auth import admin_auth
from app.controller.order_controller import (
    place_order,
    all_orders,
    user_orders,
    update_status
)

order_bp = Blueprint('order', __name__, url_prefix='/api/orders')

@order_bp.route('/list', methods=['POST'])
@admin_auth
def list_orders():
    return all_orders(request)

@order_bp.route('/status', methods=['POST'])
@admin_auth
def update_order_status():
    return update_status(request)

@order_bp.route('/place', methods=['POST'])
@auth_user
def place_order_route():
    return place_order(request)

@order_bp.route('/userorders', methods=['POST'])
@auth_user
def get_user_orders():
    return user_orders(request)

