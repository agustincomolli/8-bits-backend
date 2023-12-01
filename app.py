from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from config import get_database_uri
from flask_cors import CORS

app = Flask(__name__)
# Esto permite a todas las rutas aceptar solicitudes de origen cruzado. Para
# producción, deberías limitar esto a orígenes conocidos.
CORS(app)

# Configura la base de datos aquí
app.config['SQLALCHEMY_DATABASE_URI'] = get_database_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Service(db.Model):
    """
    Modelo de la tabla 'services' en la base de datos.

    Este modelo representará los registros de la tabla 'services'.
    Cada atributo de la clase es un campo en la tabla de la base de datos.

    Attributes:
        id (Column): Es la clave primaria.
        name (Column): Nombre del servicio. No puede ser nulo.
        description (Column): Descripción del servicio.
    """
    # Nombre de la tabla en la base de datos a la que este modelo esta ligado.
    __tablename__ = "services"
    # Identificador único de la persona. Es la llave primaria de la tabla.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)


class PlanDetail(db.Model):
    """
    Modelo para la tabla 'plan_details' en la base de datos.
    
    Representa un detalle específico asociado con un plan. Cada plan puede tener
    muchos detalles asociados que lo describen o proporcionan información adicional.
    
    Attributes:
        id (Column): Es la clave primaria.
        id_plan (Column): La clave foránea que referencia al ID del plan asociado.
        name (Column): Descripción del detalle del plan. Puede ser nulo.
    """
    __tablename__ = 'plan_details'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='Primary Key')
    id_plan = db.Column(db.Integer, db.ForeignKey('plans.id'), nullable=False)  # Se añade la relación de clave foránea
    name = db.Column(db.String(255), default=None)

    # Definición del backref para una relación bidireccional
    plan = db.relationship('Plan', back_populates='details') 


class Plan(db.Model):
    """
    Modelo para la tabla 'plans' en la base de datos.
    
    Representa los diversos planes que se pueden ofrecer a los usuarios. Cada plan
    incluye detalles específicos para diferenciarlo y proveer información a los usuarios de lo que se incluye.
    
    Attributes:
        id (Column): Es la clave primaria.
        name (Column): El nombre del plan. No puede ser nulo.
        price (Column): El precio del plan.
        subscription_time (Column): La duración de la suscripción del plan.
        description (Column): Una descripción opcional del plan.
        valid_time (Column): El tiempo de validez del plan después de la compra.
        details (relationship): Una relación que refiere a todos los detalles asociados con un plan específico.
    """
    __tablename__ = 'plans'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, comment='Primary Key')
    name = db.Column(db.String(50), nullable=False, comment='Plan Name')
    price = db.Column(db.Numeric(10, 2), nullable=False, default=0.00, comment='Plan Price')
    subscription_time = db.Column(db.String(50), default=None, comment='Subscription Duration')
    description = db.Column(db.String(255), default=None, comment='Plan Description')
    valid_time = db.Column(db.String(50), default=None, comment='Valid Time Frame')
    # Esto agregará un atributo 'details' al modelo 'Plan', que contendrá una lista de instancias de 'PlanDetail'
    details = db.relationship('PlanDetail', order_by=PlanDetail.id,
                              back_populates='plan', cascade="all, delete-orphan")


@app.route('/services', methods=['GET'])
def get_services():
    """Endpoint para obtener todos los servicios."""
    services = Service.query.all()
    service_list = []
    for service in services:
        service_dict = {'id': service.id, 'name': service.name, 'description': service.description}
        service_list.append(service_dict)
    return jsonify(service_list)


@app.route('/service/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Endpoint para obtener un servicio específico por su ID."""
    service = Service.query.get_or_404(service_id)
    return jsonify({'id': service.id, 'name': service.name, 'description': service.description})


@app.route('/service', methods=['POST'])
def add_service():
    """Endpoint para agregar un nuevo servicio."""
    data = request.json
    new_service = Service(name=data['name'], description=data.get('description'))
    db.session.add(new_service)
    db.session.commit()
    return jsonify({'id': new_service.id, 'name': new_service.name, 'description': new_service.description}), 201


@app.route('/service/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """Endpoint para actualizar un servicio existente."""
    service = Service.query.get_or_404(service_id)
    data = request.json
    service.name = data['name']
    service.description = data.get('description')
    db.session.commit()
    return jsonify({'id': service.id, 'name': service.name, 'description': service.description})


@app.route('/service/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """Endpoint para eliminar un servicio."""
    service = Service.query.get_or_404(service_id)
    db.session.delete(service)
    db.session.commit()
    return jsonify({}), 204


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear tablas si no existen
    app.run(host="0.0.0.0", debug=True)