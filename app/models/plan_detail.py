from app import db
# from app.models.plan import Plan  # Import sólo si se usan referencias a este modelo

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
