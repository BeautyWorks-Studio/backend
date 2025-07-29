from extensions import db

class Service(db.Model):
    __tablename__="services"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    bookings = db.relationship('Booking', backref='service', lazy=True)
