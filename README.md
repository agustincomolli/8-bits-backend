# 8 Bits Backend API

## Descripción

API de backend construida con Python y Flask, implementando Flask-SQLAlchemy como ORM para la gestión de una base de datos MySQL. Está diseñada para manejar las operaciones entre los diferentes modelos y proporcionar endpoints para la autenticación y el manejo de servicios y planes de mantenimiento. La API está alojada en Railway para un fácil acceso y prueba de las funcionalidades.

## Estructura del Proyecto

El código del proyecto sigue la siguiente estructura de archivos y directorios:
.
├── .gitignore
├── LICENSE
├── main.py
├── Procfile
├── README.md
├── requirements.txt
└── app
    ├── config.py
    ├── __init__.py
    ├── models
    │   ├── plan.py
    │   ├── plan_detail.py
    │   ├── service.py
    │   └── __init__.py
    ├── static
    │   ├── assets
    │   │   └── images
    │   │       └── 404.gif
    │   └── css
    │       └── error-404.css
    ├── templates
    │   └── error-404.html
    └── views
        ├── auth_routes.py
        ├── service_routes.py
        └── __init__.py

## Instalación

Para ejecutar esta API localmente, necesita seguir estos pasos:

1. Clone el repositorio.
2. Cree un ambiente virtual: `python -m venv venv`.
3. Active el ambiente virtual: `source venv/bin/activate` (Linux/Mac) o `.\venv\Scripts\activate` (Windows).
4. Instale las dependencias: `pip install -r requirements.txt`.
5. Configure las variables de entorno según necesite, o ajuste el archivo `config.py`.
6. Ejecute la aplicación: `python main.py`, según su configuración de entrada.

## Uso

Una vez iniciado el servidor, la API estará accesible desde `localhost:5000`. Asegúrese de revisar los endpoints disponibles definidos en `views/auth_routes.py` y `views/service_routes.py`.

## Despliegue

Esta API viene con un `Procfile`, preparada para el despliegue en plataformas como Heroku o Railway. Asegúrese de seguir la documentación de la plataforma de despliegue para configurar su proyecto correctamente.

## Contribución

Las contribuciones son siempre bienvenidas. Por favor, lea las directrices de contribución primero y proponga sus cambios mediante Pull Requests.

## Licencia

Este proyecto está licenciado bajo la licencia MIT; vea el archivo `LICENSE` en el repositorio para los detalles completos.

## Contacto

Si tiene alguna pregunta o comentario sobre la API, no dude en ponerse en contacto a través de [correo](mailto:agustincomolli@gmail.com).

## API Desplegada

Puede acceder a la versión desplegada de la API en: [8 Bits Backend API](https://8-bits-backend-production.up.railway.app)

---
README generado por [agustincomolli](https://github.com/agustincomolli).