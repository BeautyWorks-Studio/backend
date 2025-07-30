from flask import request, jsonify
from app.models.employee_model import Employee

def create_employee():
    data = request.get_json()
    employee = Employee(**data).save()
    return jsonify({"success": True, "message": "Employee added", "id": str(employee.id)})

def list_employees():
    employees = Employee.objects()
    return jsonify({"success": True, "employees": [e.to_mongo().to_dict() for e in employees]})