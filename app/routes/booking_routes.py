from flask import Blueprint, request, jsonify
from extensions import db
from app.models.booking import Booking
from app.models.service import Service
from app.models.user import User
from app.models.employee import Employee

booking_bp = Blueprint('booking_bp', __name__)

@booking_bp.route('/', methods=['GET'])
def get_bookings():
    bookings = Booking.query.all()
    return jsonify([
        {
            'id': b.id,
            'user_id': b.user_id,
            'service_id': b.service_id,
            'employee_id': b.employee_id,
            'table_id': b.table_id,
            'date': b.date.isoformat(),
            'status': b.status
        } for b in bookings
    ])

@booking_bp.route('/', methods=['POST'])
def create_booking():
    data = request.get_json()
    booking = Booking(
        user_id=data['user_id'],
        service_id=data['service_id'],
        employee_id=data['employee_id'],
        table_id=data.get('table_id'),
        date=data['date'],
        status=data.get('status', 'pending')
    )
    db.session.add(booking)
    db.session.commit()
    return jsonify({'message': 'Booking created', 'booking_id': booking.id}), 201
