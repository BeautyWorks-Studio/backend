from flask import Blueprint, request, jsonify
from config import db
from models.tables import Table

table_bp = Blueprint('table_bp', __name__)

@table_bp.route('/', methods=['GET'])
def get_tables():
    tables = Table.query.all()
    return jsonify([{'id': t.id, 'name': t.name, 'capacity': t.capacity} for t in tables])

@table_bp.route('/', methods=['POST'])
def create_table():
    data = request.get_json()
    table = Table(name=data['name'], capacity=data['capacity'])
    db.session.add(table)
    db.session.commit()
    return jsonify({'message': 'Table created'}), 201
