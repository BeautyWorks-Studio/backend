from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from app.extensions import init_db

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)

    init_db(app)

    from app.routes.auth_routes import auth_bp
    from app.routes.product_routes import product_bp
    from app.routes.cart_routes import cart_bp
    from app.routes.order_routes import order_bp
    from app.routes.booking_routes import booking_bp
    from app.routes.service_routes import service_bp
    from app.routes.employee_routes import employee_bp
    from app.routes.payment_routes import payment_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(product_bp, url_prefix="/api/product")
    app.register_blueprint(cart_bp, url_prefix="/api/cart")
    app.register_blueprint(order_bp, url_prefix="/api/order")
    app.register_blueprint(booking_bp, url_prefix="/api/booking")
    app.register_blueprint(service_bp, url_prefix="/api/service")
    app.register_blueprint(employee_bp, url_prefix="/api/employee")
    app.register_blueprint(payment_bp, url_prefix="/api/payment")

    @app.route("/")
    def index():
        return {"message": "Backend API is running!"}

    return app

