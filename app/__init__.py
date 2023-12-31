from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import get_database_uri

app = Flask(__name__)
app.secret_key = "clave_secreta_muy_larga"
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = get_database_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Importar las vistas para registrar las rutas
from app.views.service_routes import service_routes
from app.views.auth_routes import auth_routes
from app.views.plans_routes import plans_routes

# Registrar el blueprint para las rutas del servicio
app.register_blueprint(service_routes)
app.register_blueprint(auth_routes)
app.register_blueprint(plans_routes)

@app.errorhandler(404)
def not_found_endpoint(error):
    """
    Renderiza la plantilla "error-404.html" con el error proporcionado.

    Args:
        error: El error que ocurrió.

    Returns:
        La plantilla renderizada con el error.

    """
    return render_template("error-404.html", error=error)
