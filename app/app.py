from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


def get_database_uri():
    user = 'root'
    password = 'eggh-22cgFb-gBg4aH6DfFAC14edeFC6'
    db_name = 'railway'
    host = 'viaduct.proxy.rlwy.net'
    port = 51991

    return f'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}'


app = Flask(__name__)

# Configuración de la base de datos
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:eggh-22cgFb-gBg4aH6DfFAC14edeFC6@viaduct.proxy.rlwy.net:51991/railway'
app.config['SQLALCHEMY_DATABASE_URI'] = get_database_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db = SQLAlchemy(app)

# Definir el modelo de la tabla 'persons'


class Person(db.Model):
    __tablename__ = 'persons'  # Agrega esta línea para especificar el nombre de la tabla
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)

# Rutas CRUD

# Lista de personas


@app.route('/')
def index():
    persons = Person.query.all()
    return render_template('index.html', persons=persons)

# Detalles de una persona


@app.route('/person/<int:id>')
def person_detail(id):
    person = Person.query.get(id)
    return render_template('person_detail.html', person=person)

# Crear nueva persona


@app.route('/add_person', methods=['GET', 'POST'])
def add_person():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        new_person = Person(name=name, age=age)
        db.session.add(new_person)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_person.html')

# Actualizar persona


@app.route('/edit_person/<int:id>', methods=['GET', 'POST'])
def edit_person(id):
    person = Person.query.get(id)
    if request.method == 'POST':
        person.name = request.form['name']
        person.age = request.form['age']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_person.html', person=person)

# Eliminar persona


@app.route('/delete_person/<int:id>')
def delete_person(id):
    person = Person.query.get(id)
    db.session.delete(person)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    # db.create_all()  # Crear tablas en la base de datos si no existen
    app.run(debug=True)
