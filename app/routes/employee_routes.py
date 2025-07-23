from flask import Blueprint

employee_bp = Blueprint('employee_bp', __name__)

@employee_bp.route('/employees')
def get_employees():
    return {"message": "Employees route working"}
