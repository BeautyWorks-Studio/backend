from config import db

class Employee(db.Model):
    __tablename__="employees"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    bookings = db.relationship('Booking', backref='employee', lazy=True)
