from extensions import db 


class Product(db.Model):
    __tablename__="products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    order_items = db.relationship('OrderItem', backref='product', lazy=True)
