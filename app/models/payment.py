from mongoengine import Document, StringField, FloatField, DateTimeField
from datetime import datetime

class Payment(Document):
    __tablename__="payments"
    order_id = StringField(required=True)
    method = StringField(required=True) 
    transaction_id = StringField()
    amount = FloatField(required=True)
    status = StringField(default="pending")
    created_at = DateTimeField(default=datetime.utcnow)
