"""
Módulo principal de la aplicación.

Este módulo debe ser ejecutado para iniciar la aplicación en un servidor web montado 
en todas las direcciones IP disponibles (host="0.0.0.0").

Si el modo debug está activado, proporciona un depurador interactivo en las páginas de error 
y representaciones detalladas de los objetos de solicitud.

Nota:
    Este código debería idealmente ser ejecutado en un entorno protegido y seguro, como un contenedor.

"""

from app import app

if __name__ == '__main__':
    # Inicia el servidor. Permite el acceso a cualquier IP, no solo al localhost (host="0.0.0.0")
    # Ejecuta la aplicación en modo de depuración, lo cual proporciona páginas de error detalladas
    app.run(host="0.0.0.0", debug=True)