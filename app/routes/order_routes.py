from flask import Blueprint, request, jsonify
from app.middleware.auth import auth_user
from app.middleware.admin_auth import admin_auth
from app.controllers.order_controller import (
    place_order, place_order_stripe, place_order_razorpay,
    all_orders, user_orders, update_status,
    verify_stripe, verify_razorpay
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

@order_bp.route('/stripe', methods=['POST'])
@auth_user
def stripe_order():
    return place_order_stripe(request)

@order_bp.route('/razorpay', methods=['POST'])
@auth_user
def razorpay_order():
    return place_order_razorpay(request)

@order_bp.route('/userorders', methods=['POST'])
@auth_user
def get_user_orders():
    return user_orders(request)

@order_bp.route('/verifyStripe', methods=['POST'])
@auth_user
def verify_stripe_route():
    return verify_stripe(request)

@order_bp.route('/verifyRazorpay', methods=['POST'])
@auth_user
def verify_razorpay_route():
    return verify_razorpay(request)
