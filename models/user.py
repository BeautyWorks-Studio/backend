from mongoengine import Document, StringField, DictField, EmailField

class User(Document):
    __tablename__="users"
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    cart_data = DictField(default={})
    role = StringField(default="customer") 