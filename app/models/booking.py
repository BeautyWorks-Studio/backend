from mongoengine import Document, StringField, DateTimeField
from datetime import datetime

class Booking(Document):
    __tablename__="bookings"
    user_id = StringField(required=True)
    employee_id = StringField()
    service_id = StringField(required=True)
    scheduled_at = DateTimeField(required=True)
    status = StringField(default="pending") 
    created_at = DateTimeField(default=datetime.utcnow)
