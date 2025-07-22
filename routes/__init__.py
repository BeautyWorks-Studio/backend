from .auth_routes import auth_bp
from .product_routes import product_bp
from .order_routes import order_bp
from .booking_routes import booking_bp
from .employee_routes import employee_bp
from .

def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(product_bp, url_prefix='/products')
    app.register_blueprint(order_bp, url_prefix='/orders')
    app.register_blueprint(booking_bp, url_prefix='/bookings')
    app.register_blueprint(employee_bp, url_prefix='/employees')
    # app.register_blueprint(payment_bp, url_prefix='/payments')
    # app.register_blueprint(service_bp, url_prefix='/services')
    # app.register_blueprint(user_bp, url_prefix='/users')

