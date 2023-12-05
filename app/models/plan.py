from app import db
from app.models.plan_detail import PlanDetail

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
