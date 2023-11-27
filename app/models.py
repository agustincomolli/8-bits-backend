from app import db


class Person(db.Model):
    """
    Modelo de la tabla 'persons' en la base de datos.

    Este modelo representará los registros de la tabla 'persons'.
    Cada atributo de la clase es un campo en la tabla de la base de datos.

    Attributes:
        id (Column): Identificador único de cada persona. Es la llave primaria en la base de datos.
        name (Column): Nombre de la persona. No puede ser nulo.
        age (Column): Edad de la persona. No puede ser nulo.
    """

    # Nombre de la tabla en la base de datos a la que este modelo esta ligado.
    __tablename__ = 'persons'
    # Definición de los campos/Columnas de la tabla 'persons':
    # Identificador único de la persona. Es la llave primaria de la tabla.
    id = db.Column(db.Integer, primary_key=True)
    # Nombre de la persona. No puede ser nulo.
    name = db.Column(db.String(255), nullable=False)
    # Edad de la persona. No puede ser nulo.
    age = db.Column(db.Integer, nullable=False)
