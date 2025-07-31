from flask import request, jsonify
from flask_bcrypt import Bcrypt
import jwt, os
from app.models.user import User
from mongoengine.errors import NotUniqueError

bcrypt = Bcrypt()

def create_token(user_id):
    return jwt.encode({"id": str(user_id)}, os.getenv("JWT_SECRET"), algorithm="HS256")

def register_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"success": False, "message": "Missing fields"}), 400

    try:
        hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
        user = User(name=name, email=email, password=hashed_pw).save()
        token = create_token(user.id)
        return jsonify({"success": True, "token": token}), 201
    except NotUniqueError:
        return jsonify({"success": False, "message": "User already exists"}), 409

def login_user():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.objects(email=email).first()
    if not user:
        return jsonify({"success": False, "message": "User not found"}), 404

    if bcrypt.check_password_hash(user.password, password):
        token = create_token(user.id)
        return jsonify({"success": True, "token": token})
    else:
        return jsonify({"success": False, "message": "Invalid credentials"}), 401
