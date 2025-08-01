from functools import wraps
from flask import request, jsonify

def auth_user(func):
    """
    Middleware to protect user routes.
    Checks for a Bearer token in the Authorization header.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token or not token.startswith("Bearer "):
            return jsonify({"error": "Unauthorized - Token missing"}), 401

        user_token = token.split("Bearer ")[1].strip()

        if user_token != "user-secret-token":
            return jsonify({"error": "Unauthorized - Invalid token"}), 401

        return func(*args, **kwargs)

    return wrapper

token_required = auth_user
