from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps
from flask import jsonify

def role_required(role):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get("role") != role:
                return jsonify(msg="Access denied: insufficient permissions"), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator
