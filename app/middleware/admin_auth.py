from functools import wraps
from flask import request, jsonify

def admin_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token != 'Bearer admin-secret-token':
            return jsonify({'error': 'Unauthorized'}), 401
        return func(*args, **kwargs)
    return wrapper
