from flask import Blueprint, jsonify

service_bp = Blueprint("service_bp", __name__)

@service_bp.route("/", methods=["GET"])
def get_services():
    return jsonify({"success": True, "message": "Service routes working"})
