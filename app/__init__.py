from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
import os

from config import Config
from extensions import db, migrate, bcrypt, jwt  
from models.user import User
from models.employee import Employee
from models.service import Service
from models.booking import Booking
from models.tables import Table

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    print("📦 Using DB:", app.config["SQLALCHEMY_DATABASE_URI"])
    app.config.from_object(Config)
    print("Using DB:", app.config["SQLALCHEMY_DATABASE_URI"])

   
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    CORS(app)

    from models.user import User
    from models.employee import Employee
    from models.service import Service
    from models.booking import Booking
    from models.tables import Table

    
     

    from app.routes.auth_routes import auth_bp
    from app.routes.product_routes import product_bp
    from app.routes.order_routes import order_bp
    from app.routes.booking_routes import booking_bp
    from app.routes.employee_routes import employee_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(order_bp, url_prefix='/api/orders')
    app.register_blueprint(booking_bp, url_prefix='/api/bookings')
    app.register_blueprint(employee_bp, url_prefix='/api/employees')

    @app.route("/")
    def index():
        return {"message": "Backend API is running!"}

    return app

