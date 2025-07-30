from flask import request, jsonify
from app.models.service_model import Service

def create_service():
    data = request.get_json()
    service = Service(**data).save()
    return jsonify({"success": True, "message": "Service created", "id": str(service.id)})

def list_services():
    services = Service.objects()
    return jsonify({"success": True, "services": [s.to_mongo().to_dict() for s in services]})