class Booking(db.Model):
    __tablename__ = "booking"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    employee_id = db.Column(db.Integer, db.ForeignKey("employee.id"))
    service_id = db.Column(db.Integer, db.ForeignKey("service.id"))
    time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='pending') 

    payment = db.relationship("Payment", backref="booking", uselist=False)
