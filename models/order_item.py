from extensions import db

class OrderItem(db.Model):
    __tablename__="orderitems"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)