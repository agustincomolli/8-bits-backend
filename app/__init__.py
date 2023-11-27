from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import get_database_uri

# Se crea una instancia de la Clase Flask
app = Flask(__name__)
# Se configura la URI de la base de datos utilizando la función get_database_uri() del módulo config
app.config['SQLALCHEMY_DATABASE_URI'] = get_database_uri()
# Se desactiva el seguimiento de modificaciones de SQLAlchemy, para mejorar el rendimiento
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa la extensión SQLAlchemy para esta instancia de la aplicación
db = SQLAlchemy(app)

# Importamos las rutas y los modelos de la aplicación
# Esto se hace después de inicializar la extensión SQLAlchemy
# para evitar problemas con las referencias circulares
from app import routes, models