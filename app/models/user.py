from mongoengine import Document, StringField, EmailField, DictField

class User(Document):
    username = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    cart_data = DictField(default=dict)

    meta = {
        'collection': 'users'
    }

