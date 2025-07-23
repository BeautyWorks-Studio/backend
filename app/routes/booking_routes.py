from flask import Blueprint

booking_bp = Blueprint('booking_bp', __name__)

@booking_bp.route('/bookings')
def get_bookings():
    return {"message": "Bookings route working"}
