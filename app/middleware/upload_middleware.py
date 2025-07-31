from functools import wraps
from flask import request

def handle_uploads(fields):
    """
    Decorator to handle file uploads.
    fields: list of expected file field names.
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print("Handling file upload...")
            for field in fields:
                if field in request.files:
                    file = request.files[field]
                    print(f"Received file for {field}: {file.filename}")
            return f(*args, **kwargs)
        return wrapper
    return decorator

