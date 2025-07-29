from extensions import db 

class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    role = db.Column(db.String(50)) 


    services = db.relationship("EmployeeService", back_populates="employee")
    bookings = db.relationship("Booking", backref="employee")
