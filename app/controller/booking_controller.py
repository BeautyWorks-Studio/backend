from flask import request, jsonify
from app.models.booking_model import Booking
from datetime import datetime
from app.middleware.auth import token_required

@token_required
def create_booking():
    data = request.get_json()
    booking = Booking(
        user_id=request.user_id,
        employee_id=data.get("employeeId"),
        service_id=data.get("serviceId"),
        scheduled_at=datetime.fromisoformat(data.get("scheduledAt"))
    ).save()
    return jsonify({"success": True, "message": "Booking created", "id": str(booking.id)})

@token_required
def user_bookings():
    bookings = Booking.objects(user_id=request.user_id)
    return jsonify({"success": True, "bookings": [b.to_mongo().to_dict() for b in bookings]})

def all_bookings():
    bookings = Booking.objects()
    return jsonify({"success": True, "bookings": [b.to_mongo().to_dict() for b in bookings]})