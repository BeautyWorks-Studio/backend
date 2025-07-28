class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=True)
    booking_id = db.Column(db.Integer, db.ForeignKey("booking.id"), nullable=True)
    payment_method = db.Column(db.String(50))  # e.g., card, M-Pesa
    amount = db.Column(db.Float)
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)
