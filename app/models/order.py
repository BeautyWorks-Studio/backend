from mongoengine import Document, StringField, ListField, EmbeddedDocumentField, FloatField, BooleanField, DateTimeField
from .order_item import OrderItem
from datetime import datetime

class Order(Document):
    __tablename__="orders"
    user_id = StringField(required=True)
    items = ListField(EmbeddedDocumentField(OrderItem))
    amount = FloatField(required=True)
    address = StringField(required=True)
    status = StringField(default="Order Placed")
    payment_method = StringField(required=True)   
    payment_status = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.utcnow)
