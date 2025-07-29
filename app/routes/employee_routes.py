from flask import Blueprint, request, jsonify
from extensions import db
from models.employee import Employee

employee_bp = Blueprint('employee_bp', __name__)

@employee_bp.route('/', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([
        {
            'id': e.id,
            'name': e.name,
            'role': e.role,
            'email': e.email,
            'phone': e.phone
        } for e in employees
    ])

@employee_bp.route('/', methods=['POST'])
def create_employee():
    data = request.get_json()
    employee = Employee(
        name=data['name'],
        role=data['role'],
        email=data['email'],
        phone=data['phone']
    )
    db.session.add(employee)
    db.session.commit()
    return jsonify({'message': 'Employee created', 'employee_id': employee.id}), 201
