from flask import Blueprint, jsonify, request
from app.models.plan import Plan
from app import db

# Creación de un nuevo Blueprint para las rutas de autenticación
plans_routes = Blueprint("plans_routes", __name__)


@plans_routes.route('/plans', methods=['GET'])
def get_plans():
    """Endpoint para obtener todos los planes de mantenimiento."""
    plans = Plan.query.all()
    plan_list = []
    for plan in plans:
        plan_dict = {'id': plan.id, 
                     'name': plan.name, 
                     'price': plan.price,
                     'subscription_time': plan.subscription_time,
                     'description': plan.description,
                     'valid_time': plan.valid_time,
                     'details': [
                         {'id': detail.id, 'name': detail.name}
                         for detail in plan.details
                     ]}
        plan_list.append(plan_dict)
    return jsonify(plan_list)


@plans_routes.route('/plan/<int:plan_id>', methods=['GET'])
def get_plan(plan_id):
    """Endpoint para obtener un plan específico por su ID."""
    plan = Plan.query.get_or_404(plan_id)
    return jsonify({'id': plan.id, 'name': plan.name, 'price': plan.price})
