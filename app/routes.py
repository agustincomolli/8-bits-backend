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

    return render_template('admin-services.html', **context)


@app.route("/add-service", methods=["GET", "POST"])
def add_service():
    """
    Ruta para agregar un nuevo servicio.

    Método GET:
    Muestra el formulario para agregar un nuevo servicio.

    Método POST:
    Procesa el formulario enviado, crea un nuevo servicio y lo agrega a la base de datos.

    Returns:
    - GET: Renderiza el formulario para agregar un servicio.
    - POST: Redirecciona a la página principal después de agregar el servicio.
    """
    if request.method == "POST":
        # Obtiene los datos del formulario enviado por el método POST
        name = request.form["name"]
        description = request.form["description"]

        # Crea un nuevo objeto Service con los datos proporcionados
        new_service = Service(name=name, description=description)

        # Agrega el nuevo servicio a la sesión de la base de datos
        db.session.add(new_service)

        # Guarda los cambios en la base de datos
        db.session.commit()

        # Redirecciona a la página principal después de agregar el servicio
        return redirect(url_for("index"))
    
    context = {
        "title": "Agrega un nuevo servicio",
    }
    # Renderiza el formulario para agregar un servicio (Método GET)
    return render_template("service.html", **context)