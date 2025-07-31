from flask import request, jsonify
from app.models.user import User
from app.middleware.auth import token_required


@token_required
def get_cart():
    """Get the current user's cart"""
    user = User.objects(id=request.user_id).first()
    if not user:
        return jsonify({"success": False, "message": "User not found"}), 404
    return jsonify({"success": True, "cartData": user.cart_data})


@token_required
def add_to_cart():
    """Add an item to the cart"""
    data = request.get_json()
    item_id = data.get("itemId")
    size = data.get("size")

    user = User.objects(id=request.user_id).first()
    if not user:
        return jsonify({"success": False, "message": "User not found"}), 404

    cart = user.cart_data or {}

    if item_id not in cart:
        cart[item_id] = {}

    cart[item_id][size] = cart[item_id].get(size, 0) + 1

    user.cart_data = cart
    user.save()

    return jsonify({"success": True, "message": "Added to cart"})


@token_required
def update_cart():
    """Update the quantity of an item in the cart"""
    data = request.get_json()
    item_id = data.get("itemId")
    size = data.get("size")
    quantity = data.get("quantity")

    user = User.objects(id=request.user_id).first()
    if not user:
        return jsonify({"success": False, "message": "User not found"}), 404

    cart = user.cart_data or {}

    if item_id in cart and size in cart[item_id]:
        cart[item_id][size] = quantity
        user.cart_data = cart
        user.save()
        return jsonify({"success": True, "message": "Cart updated"})

    return jsonify({"success": False, "message": "Item not found"}), 404

