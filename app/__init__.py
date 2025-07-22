from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    # Load environment variables from .env
    load_dotenv()

    app = Flask(__name__)

    # Load configuration from config file
    app.config.from_object('app.config.Config')

    # Initialize extensions with app
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.product_routes import product_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(product_bp, url_prefix='/api/products')

    # Add a default root route for status checking
    @app.route("/")
    def index():
        return {"message": "Backend API is running!"}

    # Create tables if they don't exist
    with app.app_context():
        db.create_all()

    return app

