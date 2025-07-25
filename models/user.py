from config import db
from app import bcrypt
from sqlalchemy.orm import relationship
from datetime import datetime

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    country = db.Column(db.String(100))
    role = db.Column(db.String(20), default='user')  # 'admin', 'staff', 'user'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    orders = relationship('Order', backref='user', lazy=True)
    bookings = relationship('Booking', backref='user', lazy=True)

    def __init__(self, name, email, password_hash,phone=None, address=None, country=None, role='user'):
        self.name = name
        self.email = email
        self.password_hash = bcrypt.generate_password_hash(password_hash).decode('utf-8')
        self.phone = phone
        self.address = address
        self.country = country
        self.role = role

    def check_password(self, password_hash):
        return bcrypt.check_password_hash(self.password_hash, password_hash)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "created_at": self.created_at
        }

