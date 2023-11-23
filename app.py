from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Configura la conexión a la base de datos
db = pymysql.connect(host="viaduct.proxy.rlwy.net", port=51991, user="root", password="eggh-22cgFb-gBg4aH6DfFAC14edeFC6", database="servicios")
cursor = db.cursor()

# Ruta para la página principal
@app.route('/')
def index():
    # Obtén los datos de la base de datos
    cursor.execute("SELECT id, servicio_nombre, servicio_descripcion FROM servicios_info")
    data = cursor.fetchall()
    return render_template('index.html', servicios=data)

# Ruta para la página de creación
@app.route('/create')
def create():
    return render_template('create.html')

# Ruta para manejar la creación de un nuevo servicio
@app.route('/create_process', methods=['POST'])
def create_process():
    nombre = request.form['servicio_nombre']
    descripcion = request.form['servicio_descripcion']
    
    # Inserta los datos en la base de datos
    cursor.execute("INSERT INTO servicios_info (servicio_nombre, servicio_descripcion) VALUES (%s, %s)", (nombre, descripcion))
    db.commit()

    return redirect(url_for('index'))

# Ruta para la página de actualización
@app.route('/update/<int:servicio_id>')
def update(servicio_id):
    cursor.execute("SELECT id, servicio_nombre, servicio_descripcion FROM servicios_info WHERE id = %s", servicio_id)
    data = cursor.fetchone()
    return render_template('update.html', servicio=data)

# Ruta para manejar la actualización de un servicio
@app.route('/update_process/<int:servicio_id>', methods=['POST'])
def update_process(servicio_id):
    nombre = request.form['servicio_nombre']
    descripcion = request.form['servicio_descripcion']
    
    # Actualiza los datos en la base de datos
    cursor.execute("UPDATE servicios_info SET servicio_nombre=%s, servicio_descripcion=%s WHERE id=%s", (nombre, descripcion, servicio_id))
    db.commit()

    return redirect(url_for('index'))

# Ruta para manejar la eliminación de un servicio
@app.route('/delete/<int:servicio_id>')
def delete(servicio_id):
    # Elimina el servicio de la base de datos
    cursor.execute("DELETE FROM servicios_info WHERE id=%s", servicio_id)
    db.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
