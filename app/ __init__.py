from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from app.routes.auth_routes import auth_bp
    from app.routes.product_routes import product_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(product_bp, url_prefix='/api/products')

    with app.app_context():
        db.create_all()

    return app
