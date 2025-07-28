class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    availability = db.Column(db.Text)  # e.g., JSON or text for schedules

    services = db.relationship("EmployeeService", back_populates="employee")
    bookings = db.relationship("Booking", backref="employee")
