from flask import Flask, render_template, request, redirect, url_for, session
import pymysql

# Creamos la aplicación Flask y configuramos la clave secreta para las sesiones
app = Flask(__name__)
# Asegúrate de cambiar esto por una clave más segura.
app.secret_key = 'TURANDOMKEY'

# Configuramos la conexión a database de MySQL con PyMySQL
db = pymysql.connect(host="viaduct.proxy.rlwy.net", port=51991, user="root",
                     password="eggh-22cgFb-gBg4aH6DfFAC14edeFC6", database="servicios")
cursor = db.cursor()


@app.route('/', methods=['GET', 'POST'])
def login():
    """
    La ruta para el inicio de sesión.
    Permite al usuario ingresar sus credenciales para iniciar sesión.
    """
    error = None
    if 'username' in session:
        # Si el usuario ya está logueado, redirigir al índice
        return redirect(url_for('index'))
    if request.method == 'POST':
        # Verificar la información del formulario
        if request.form['username'] != 'Administrador' or request.form['password'] != 'Contraseña':
            error = 'Invalid Credentials. Please try again.'
        else:
            # Si las credenciales son correctas, iniciar sesión y redirigir al índice
            session['username'] = request.form['username']
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    """
    La ruta para cerrar la sesión.
    Termina la sesión del usuario y redirige a la página de inicio de sesión.
    """
    session.pop('username', None)
    return redirect(url_for('login'))


# Ruta para la página principal
@app.route('/index')
def index():
    """
    La ruta index muestra todos los servicios si el usuario ha iniciado sesión.
    Si el usuario no está logueado, será redirigido al inicio de sesión.
    """
    if 'username' in session:
        cursor.execute(
            "SELECT id, servicio_nombre, servicio_descripcion FROM servicios_info")
        data = cursor.fetchall()
        return render_template('index.html', servicios=data)
    else:
        return redirect(url_for('login'))


# Ruta para la página de creación
@app.route('/create')
def create():
    """
    La ruta create muestra la página de creación si el usuario ha iniciado sesión.
    Si el usuario no está logueado, será redirigido al inicio de sesión.
    """
    if 'username' in session:
        return render_template('create.html')
    else:
        return redirect(url_for('login'))


# Ruta para manejar la creación de un nuevo servicio
@app.route('/create_process', methods=['POST'])
def create_process():
    """
    Esta ruta procesa los datos enviados desde la página de creación y crea un nuevo servicio en la base de datos.
    Solo usuarios logueados pueden crear servicios.
    """
    if 'username' in session:
        nombre = request.form['servicio_nombre']
        descripcion = request.form['servicio_descripcion']

        # Insertar los datos en la base de datos
        cursor.execute(
            "INSERT INTO servicios_info (servicio_nombre, servicio_descripcion) VALUES (%s, %s)", (nombre, descripcion))
        db.commit()

        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))


# Ruta para la página de actualización
@app.route('/update/<int:servicio_id>')
def update(servicio_id):
    """
    La ruta update muestra la página de actualización si el usuario ha iniciado sesión.
    Si el usuario no está logueado, será redirigido al inicio de sesión.
    """
    if 'username' in session:
        cursor.execute(
            "SELECT id, servicio_nombre, servicio_descripcion FROM servicios_info WHERE id = %s", servicio_id)
        data = cursor.fetchone()
        return render_template('update.html', servicio=data)
    else:
        return redirect(url_for('login'))


# Ruta para manejar la actualización de un servicio
@app.route('/update_process/<int:servicio_id>', methods=['POST'])
def update_process(servicio_id):
    """
    Esta ruta procesa los datos enviados desde la página de actualización y actualiza un servicio en la base de datos.
    Solo usuarios logueados pueden actualizar servicios.
    """
    if 'username' in session:
        nombre = request.form['servicio_nombre']
        descripcion = request.form['servicio_descripcion']

        # Actualizar los datos en la base de datos
        cursor.execute("UPDATE servicios_info SET servicio_nombre=%s, servicio_descripcion=%s WHERE id=%s",
                       (nombre, descripcion, servicio_id))
        db.commit()

        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))


# Ruta para manejar la eliminación de un servicio
@app.route('/delete/<int:servicio_id>')
def delete(servicio_id):
    """
    Esta ruta maneja la eliminación de un servicio de la base de datos.
    Solo usuarios logueados pueden eliminar servicios.
    """
    if 'username' in session:
        # Eliminar el servicio de la base de datos
        cursor.execute("DELETE FROM servicios_info WHERE id=%s", servicio_id)
        db.commit()

        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
