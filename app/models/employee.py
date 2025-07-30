from mongoengine import Document, StringField, EmailField, DateTimeField
from datetime import datetime

class Employee(Document):
    __tablename__="employees"
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    role = StringField(required=True)  
    hired_at = DateTimeField(default=datetime.utcnow)
