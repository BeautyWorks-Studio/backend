from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv
from config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    CORS(app)

    # Register blueprints (after creating app)
    from app.routes.auth_routes import auth_bp
    from app.routes.product_routes import product_bp
    from app.routes.booking_routes import booking_bp
    from app.routes.employee_routes import employee_bp
    from app.routes.order_routes import order_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(booking_bp, url_prefix='/api/bookings')
    app.register_blueprint(employee_bp, url_prefix='/api/employees')
    app.register_blueprint(order_bp, url_prefix='/api/orders')

    @app.route("/")
    def index():
        return {"message": "Backend API is running!"}

    return app
