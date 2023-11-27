from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Person


@app.route('/')
def index():
    """Ruta para la página principal.

    Devuelve una lista de todas las personas en la base de datos y los incluye en la plantilla 'index.html'

    Returns:
        render_template: Renderiza la plantilla 'index.html' con la lista de todas las personas.
    """
    persons = Person.query.all()
    return render_template('index.html', persons=persons)


@app.route('/person/<int:id>')
def person_detail(id):
    """Ruta para los detalles de una persona en particular.

    Recuperar una persona específica de la base de datos por su ID y la incluye en la plantilla 'person_detail.html'.

    Args:
        id (int): ID de la persona que queremos recuperar.

    Returns:
        render_template: Renderiza la plantilla 'person_detail.html' con los detalles de la persona especificada.
    """
    person = Person.query.get(id)
    return render_template('person_detail.html', person=person)


@app.route('/add_person', methods=['GET', 'POST'])
def add_person():
    """Ruta para agregar una nueva persona.

    Si el método de la solicitud es POST, esto recuperará el nombre y la edad de la persona desde el formulario de la solicitud, creará una nueva persona en la base de datos y luego redirigirá al usuario a la página principal.

    Returns:
        redirect: Redirige al usuario a la página principal después de agregar una nueva persona.
        render_template: Renderiza la plantilla 'add_person.html' si el método de la solicitud es GET.
    """
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        new_person = Person(name=name, age=age)
        db.session.add(new_person)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_person.html')


@app.route('/edit_person/<int:id>', methods=['GET', 'POST'])
def edit_person(id):
    """Ruta para editar una persona existente.

    Si el método de la solicitud es POST, esto recuperará el nombre y la edad de la persona desde el formulario de la solicitud, actualizará la persona en la base de datos y luego redirigirá al usuario a la página principal.

    Args:
        id (int): ID de la persona que queremos editar.

    Returns:
        redirect: Redirige al usuario a la página principal después de editar una persona.
        render_template: Renderiza la plantilla 'edit_person.html' si el método de la solicitud es GET.
    """
    person = Person.query.get(id)
    if request.method == 'POST':
        person.name = request.form['name']
        person.age = request.form['age']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_person.html', person=person)


@app.route('/delete_person/<int:id>')
def delete_person(id):
    """Ruta para eliminar a una persona existente.

    Recupera una persona específica de la base de datos por su ID, la elimina de la base de datos y luego redirige al usuario a la página principal.

    Args:
        id (int): ID de la persona que queremos eliminar.

    Returns:
        redirect: Redirige al usuario a la página principal después de eliminar a una persona.
    """
    person = Person.query.get(id)
    db.session.delete(person)
    db.session.commit()
    return redirect(url_for('index'))
