from flask import Blueprint, jsonify, request, session

# Creación de un nuevo Blueprint para las rutas de autenticación
auth_routes = Blueprint("auth_routes", __name__)

def validate_user(username, password) -> bool:
    """
    Valida si el usuario y la contraseña proporcionados son correctos.
    Los valores correctos son "admin" tanto para el usuario como para la contraseña en este caso simple.
    
    :param username: Nombre de usuario proporcionado.
    :param password: Contraseña proporcionada.
    :return: Booleano indicando si la validación fue exitosa.
    """
    if username == "admin" and password == "admin":
        return True
    else:
        return False
    

@auth_routes.route("/login", methods=["POST"])
def login():
    """
    Ruta para iniciar sesión. Toma los datos de usuario y contraseña del cuerpo
    de la solicitud, valida esos datos y establece el estado de inicio de sesión.
    
    :return: Una respuesta JSON que indica el éxito o fracaso del inicio de sesión,
             junto con un código de estado HTTP apropiado.
    """
    # Obtener datos de la solicitud
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # Validar usuario
    if validate_user(username, password):
        # Si la validación es exitosa, establecer la sesión como iniciada
        session["is_logged_in"] = True
        # Retornar un mensaje de éxito
        return jsonify({"status":"ok", "message":"Sesión iniciada con éxito"}), 200
    else:
        # Retornar un mensaje de error si la validación falla
        return jsonify({"status": "error", "message": "El usuario o la contraseña son inválidos"}), 401
    

@auth_routes.route("/logout", methods=["POST"])
def logout():
    """
    Ruta para cerrar sesión. Elimina el estado de inicio de sesión del usuario de la sesión.
    
    :return: Una respuesta JSON que confirma que la sesión se ha cerrado correctamente,
             junto con un código de estado HTTP.
    """
    # Eliminar el estado de inicio de sesión del usuario de la sesión
    session.pop("is_logged_in", None)
    # Retornar un mensaje de éxito
    return jsonify({"status": "ok", "message":"Se ha cerrado la sesión correctamente"}), 200