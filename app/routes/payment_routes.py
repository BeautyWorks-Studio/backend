from flask import Blueprint, jsonify

payment_bp = Blueprint("payment_bp", __name__)

@payment_bp.route("/", methods=["GET"])
def get_payments():
    return jsonify({"success": True, "message": "Payment routes working"})
