from flask import Blueprint, render_template

# Creación de un nuevo Blueprint para las rutas de autenticación
error_routes = Blueprint("error_routes", __name__)


@error_routes.errorhandler(404)
def not_found_endpoint(error):
    """
    Renderiza la plantilla "error-404.html" con el error proporcionado.

    Args:
        error: El error que ocurrió.

    Returns:
        La plantilla renderizada con el error.

    """
    return render_template("error-404.html", error=error)
