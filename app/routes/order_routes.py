from flask import Blueprint, request, jsonify
from extensions import db
from models.order import Order
from models.order_item import OrderItem
from models.product import Product

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([
        {
            'id': o.id,
            'user_id': o.user_id,
            'created_at': o.created_at.isoformat(),
            'total_amount': o.total_amount,
            'status': o.status,
            'items': [
                {
                    'product_id': item.product_id,
                    'quantity': item.quantity
                } for item in o.items
            ]
        } for o in orders
    ])

@order_bp.route('/', methods=['POST'])
def create_order():
    data = request.get_json()
    order = Order(
        user_id=data['user_id'],
        total_amount=data['total_amount'],
        status=data.get('status', 'pending')
    )
    db.session.add(order)
    db.session.flush()
    for item in data['items']:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item['product_id'],
            quantity=item['quantity']
        )
        db.session.add(order_item)
    db.session.commit()
    return jsonify({'message': 'Order created', 'order_id': order.id}), 201
