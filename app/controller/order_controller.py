from flask import request, jsonify
from app.models.order_model import Order
from app.models.user_model import User
from app.models.order_item_model import OrderItem
from datetime import datetime
from app.middleware.auth import token_required

@token_required
def place_order():
    data = request.get_json()
    items = [OrderItem(**item) for item in data.get("items")]
    address = data.get("address")
    amount = data.get("amount")

    order = Order(
        user_id=request.user_id,
        items=items,
        amount=amount,
        address=address,
        payment_method="COD",
        payment_status=False,
        created_at=datetime.utcnow()
    ).save()

  
    user = User.objects(id=request.user_id).first()
    user.cart_data = {}
    user.save()

    return jsonify({"success": True, "message": "Order placed", "orderId": str(order.id)})

@token_required
def get_user_orders():
    orders = Order.objects(user_id=request.user_id)
    return jsonify({"success": True, "orders": [o.to_mongo().to_dict() for o in orders]})

def get_all_orders():
    orders = Order.objects()
    return jsonify({"success": True, "orders": [o.to_mongo().to_dict() for o in orders]})

def update_order_status():
    data = request.get_json()
    order_id = data.get("orderId")
    status = data.get("status")

    order = Order.objects(id=order_id).first()
    if not order:
        return jsonify({"success": False, "message": "Order not found"}), 404

    order.status = status
    order.save()
    return jsonify({"success": True, "message": "Order status updated"})
