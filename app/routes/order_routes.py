from flask import Blueprint

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/orders')
def get_orders():
    return {"message": "Orders route working"}
