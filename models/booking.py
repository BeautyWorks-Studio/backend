from extensions import db

class Booking(db.Model):
    __tablename__ = "bookings"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"))
    service_id = db.Column(db.Integer, db.ForeignKey("services.id"))
    table_id = db.Column(db.Integer, db.ForeignKey('tables.id'), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='pending') 

    payment = db.relationship("Payment", back_populates="booking", uselist=False)
    table = db.relationship("Table", back_populates="bookings")
    
