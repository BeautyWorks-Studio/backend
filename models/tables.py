from extensions import db

class Table(db.Model):
    __tablename__="tables"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    capacity = db.Column(db.Integer, nullable=False)
    bookings = db.relationship('Booking', back_populates='table', lazy=True)
