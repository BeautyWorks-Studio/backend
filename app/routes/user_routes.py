from flask import Blueprint, request
from app.controller.user_controller import (
    login_user,
    register_user,
    admin_login
)

user_bp = Blueprint('user', __name__, url_prefix='/api/users')

@user_bp.route('/register', methods=['POST'])
def register():
    return register_user(request)

@user_bp.route('/login', methods=['POST'])
def login():
    return login_user(request)

@user_bp.route('/admin', methods=['POST'])
def admin():
    return admin_login(request)

