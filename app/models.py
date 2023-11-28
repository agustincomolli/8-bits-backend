from app import db


class Service(db.Model):
    """
    Modelo de la tabla 'services' en la base de datos.

    Este modelo representará los registros de la tabla 'services'.
    Cada atributo de la clase es un campo en la tabla de la base de datos.

    Attributes:
        id (Column): Identificador único de cada servicio. Es la llave primaria en la base de datos.
        name (Column): Nombre del servicio. No puede ser nulo.
        description (Column): Descripción del servicio.
    """
    # Nombre de la tabla en la base de datos a la que este modelo esta ligado.
    __tablename__ = "services"
    # Identificador único de la persona. Es la llave primaria de la tabla.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
