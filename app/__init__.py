from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from flask_migrate import Migrate

from flask_cors import CORS

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

    app = Flask(__name__)
    app.config.from_object('config.Config')

    load_dotenv()

    app = Flask(__name__)

    
    app.config.from_object('app.config.Config')

   
    CORS(app)

   
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


  
    @app.route("/")

    @app.route('/')

    def index():
        return {"message": "Backend API is running!"}

   
    # with app.app_context():
    #     db.create_all()

    # import models
=======
    # Auto-create all DB tables
    with app.app_context():
        db.create_all()


    return app
