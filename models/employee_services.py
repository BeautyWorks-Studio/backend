from extensions import db

class EmployeeService(db.Model):
    __tablename__ = 'employee_services'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'))

    employee = db.relationship("Employee", back_populates="services")
