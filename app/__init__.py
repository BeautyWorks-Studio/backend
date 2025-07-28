from flask import Flask
<<<<<<< HEAD
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
=======
from flask_cors import CORS
from dotenv import load_dotenv
from config import Config
from extensions import db, migrate, bcrypt, jwt  
from models.user import User
from models.employee import Employee
from models.service import Service
from models.booking import Booking
from models.tables import Table
# from models import *  

def create_app():
    load_dotenv()

>>>>>>> 62cc36b9109d9911316eda7ebfbc6407b76b1cd6
    app = Flask(__name__)
    app.config.from_object(Config)
    print("📦 Using DB:", app.config["SQLALCHEMY_DATABASE_URI"])

<<<<<<< HEAD
    app.config.from_object('app.config.Config')

    CORS(app)

=======
>>>>>>> 62cc36b9109d9911316eda7ebfbc6407b76b1cd6
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    CORS(app)


<<<<<<< HEAD
=======
    
     

>>>>>>> 62cc36b9109d9911316eda7ebfbc6407b76b1cd6
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

<<<<<<< HEAD
    @app.route("/")
    def index():
        return {"message": "Backend API is running!"}

    with app.app_context():
        db.create_all()

=======
    @app.route('/')
    def index():
        return {"message": "Backend API is running!"}

>>>>>>> 62cc36b9109d9911316eda7ebfbc6407b76b1cd6
    return app

