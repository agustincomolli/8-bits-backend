from app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear tablas en la base de datos si no existen
    app.run(host="0.0.0.0", debug=True)