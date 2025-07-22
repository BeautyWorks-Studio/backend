from flask import Blueprint, request, jsonify
from models import User
from app.utils.auth import create_user, authenticate
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = create_user(data['name'], data['email'], data['password'], data.get('role', 'user'))
    return jsonify({"msg": "User created", "user": {"email": user.email, "role": user.role}}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = authenticate(data['email'], data['password'])
    if user:
        token = create_access_token(identity=user.id)
        return jsonify(access_token=token, role=user.role)
    return jsonify({"msg": "Invalid credentials"}), 401
