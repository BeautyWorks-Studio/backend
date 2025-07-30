from mongoengine import EmbeddedDocument, StringField, FloatField, IntField

class OrderItem(EmbeddedDocument):
    __tablename__="order-items"
    product_id = StringField(required=True)
    name = StringField(required=True)
    price = FloatField(required=True)
    quantity = IntField(required=True)
    size = StringField()
