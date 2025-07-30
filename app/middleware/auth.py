from flask import request, jsonify
from functools import wraps
import jwt
import os

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('token')
        if not token:
            return jsonify({'success': False, 'message': 'Missing token'}), 403
        try:
            decoded = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
            request.user_id = decoded["id"]
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)}), 401
        return f(*args, **kwargs)
    return decorated
