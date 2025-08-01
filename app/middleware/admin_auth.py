from functools import wraps
from flask import request, jsonify

def admin_auth(func):
    """
    Middleware to protect admin routes.
    Checks for a Bearer token in the Authorization header.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token or not token.startswith("Bearer "):
            return jsonify({"error": "Unauthorized - Token missing"}), 401

        admin_token = token.split("Bearer ")[1].strip()

        if admin_token != "admin-secret-token":
            return jsonify({"error": "Unauthorized - Invalid admin token"}), 401

        return func(*args, **kwargs)

    return wrapper

