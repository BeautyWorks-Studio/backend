from config import db
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    country = db.Column(db.String(100))
    orders = relationship('Order', backref='user', lazy=True)
    bookings = relationship('Booking', backref='user', lazy=True)
