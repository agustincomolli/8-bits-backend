from flask import Blueprint, jsonify, request
from app.models.service import Service
from app import db

service_routes = Blueprint('service_routes', __name__)


@service_routes.route('/services', methods=['GET'])
def get_services():
    """Endpoint para obtener todos los servicios."""
    services = Service.query.all()
    service_list = []
    for service in services:
        service_dict = {'id': service.id, 'name': service.name, 'description': service.description}
        service_list.append(service_dict)
    return jsonify(service_list)


@service_routes.route('/service/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Endpoint para obtener un servicio específico por su ID."""
    service = Service.query.get_or_404(service_id)
    return jsonify({'id': service.id, 'name': service.name, 'description': service.description})


@service_routes.route('/service', methods=['POST'])
def add_service():
    """Endpoint para agregar un nuevo servicio."""
    data = request.json
    new_service = Service(name=data['name'], description=data.get('description'))
    db.session.add(new_service)
    db.session.commit()
    return jsonify({'id': new_service.id, 'name': new_service.name, 'description': new_service.description}), 201


@service_routes.route('/service/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """Endpoint para actualizar un servicio existente."""
    service = Service.query.get_or_404(service_id)
    data = request.json
    service.name = data['name']
    service.description = data.get('description')
    db.session.commit()
    return jsonify({'id': service.id, 'name': service.name, 'description': service.description})


@service_routes.route('/service/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """Endpoint para eliminar un servicio."""
    service = Service.query.get_or_404(service_id)
    db.session.delete(service)
    db.session.commit()
    return jsonify({}), 204
