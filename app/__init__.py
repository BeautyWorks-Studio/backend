from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
<<<<<<< HEAD
from flask_migrate import Migrate
=======
from flask_cors import CORS
>>>>>>> 73a97c5 (modified app/_init_.py modified app/config.py modified app/routes/auth_routes.py modified app/routes/product_routes.py)
from dotenv import load_dotenv
from config import db
from config import migrate
# import models
import os


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
<<<<<<< HEAD
    app = Flask(__name__)
    app.config.from_object('config.Config')
=======
    # Load environment variables from .env file
    load_dotenv()

    app = Flask(__name__)

    # Load configuration from config file
    app.config.from_object('app.config.Config')

    # Enable CORS (optional but useful if connecting to a frontend)
    CORS(app)

    # Initialize extensions
>>>>>>> 73a97c5 (modified app/_init_.py modified app/config.py modified app/routes/auth_routes.py modified app/routes/product_routes.py)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    
    from app.routes.auth_routes import auth_bp
    from app.routes.product_routes import product_bp
    from app.routes.order_routes import order_bp
    from app.routes.booking_routes import booking_bp
    from app.routes.employee_routes import employee_bp
    

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(booking_bp, url_prefix='/api/bookings')
    app.register_blueprint(employee_bp, url_prefix='/api/employees')

<<<<<<< HEAD
  
    @app.route("/")
=======
    # Root endpoint for health check
    @app.route('/')
>>>>>>> 73a97c5 (modified app/_init_.py modified app/config.py modified app/routes/auth_routes.py modified app/routes/product_routes.py)
    def index():
        return {"message": "Backend API is running!"}

<<<<<<< HEAD
   
    # with app.app_context():
    #     db.create_all()

    # import models
=======
    # Auto-create all DB tables
    with app.app_context():
        db.create_all()
>>>>>>> 73a97c5 (modified app/_init_.py modified app/config.py modified app/routes/auth_routes.py modified app/routes/product_routes.py)

    return app
