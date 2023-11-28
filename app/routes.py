from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Service


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
