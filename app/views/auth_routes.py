from flask import Blueprint, jsonify, request, session

auth_routes = Blueprint("auth_routes", __name__)

def validate_user(username, password) -> bool:
    if username == "admin" and password == "admin":
        return True
    else:
        return False
    

@auth_routes.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if validate_user(username, password):
        session["is_logged_in"] = True
        return jsonify({"status":"ok", "message":"Sesión iniciada con éxito"}), 200
    else:
        return jsonify({"status": "error", "message": "El usuario o la contraseña son inválidos"}), 401
    

@auth_routes.route("/logout", methods=["POST"])
def logout():
    session.pop("is_logged_in", None)
    return jsonify({"status": "ok", "message":"Se ha cerrado la sesión correctamente"}), 200