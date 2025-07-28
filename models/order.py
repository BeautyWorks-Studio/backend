from models import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # pending, shipped, delivered
    shipping_address = db.Column(db.String(255))

    items = db.relationship("OrderItem", backref="order")
    payment = db.relationship("Payment", backref="order", uselist=False)
