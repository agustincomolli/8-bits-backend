from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Service


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


@app.route('/')
def index():
    """Ruta para la página principal.

    Devuelve una lista de todas las personas en la base de datos y los incluye en la plantilla 'index.html'

    Returns:
        render_template: Renderiza la plantilla 'index.html' con la lista de todas las personas.
    """
    context = {
        "services": Service.query.all(),
    }

    return render_template('admin.html', **context)
