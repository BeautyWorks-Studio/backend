from mongoengine import Document, StringField, FloatField, ListField, BooleanField, DateTimeField
from datetime import datetime

class Product(Document):
    __tablename__="products"
    name = StringField(required=True)
    description = StringField()
    price = FloatField(required=True)
    category = StringField()
    sub_category = StringField()
    image_urls = ListField(StringField())
    sizes = ListField(StringField())
    bestseller = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.utcnow)
