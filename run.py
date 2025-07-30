from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

from config.mongodb import connect_db
from config.cloudinary import connect_cloudinary
from routes.user_route import user_bp
from routes.product_route import product_bp
from routes.cart_route import cart_bp
from routes.order_route import order_bp

app = Flask(__name__)
CORS(app)

connect_db()
connect_cloudinary()

app.register_blueprint(user_bp, url_prefix="/api/user")
app.register_blueprint(product_bp, url_prefix="/api/product")
app.register_blueprint(cart_bp, url_prefix="/api/cart")
app.register_blueprint(order_bp, url_prefix="/api/order")

@app.route("/", methods=["GET"])
def home():
    return "API Working"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 4000))
    app.run(host="0.0.0.0", port=port)
