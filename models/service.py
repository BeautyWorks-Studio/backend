from mongoengine import Document, StringField, FloatField, IntField

class Service(Document):
    __tablename__="services"
    name = StringField(required=True)
    description = StringField()
    price = FloatField(required=True)
    duration_minutes = IntField(default=30)
