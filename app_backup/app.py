from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from backend.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    from backend.routes.auth_routes import auth_bp
    from backend.routes.product_routes import product_bp
    from backend.routes.booking_routes import booking_bp
    from backend.routes.employee_routes import employee_bp
    from backend.routes.order_routes import order_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(booking_bp, url_prefix='/api/bookings')
    app.register_blueprint(employee_bp, url_prefix='/api/employees')
    app.register_blueprint(order_bp, url_prefix='/api/orders')

    return app
