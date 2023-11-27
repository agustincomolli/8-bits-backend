def get_database_uri():
    """
    Genera y devuelve la URI de la base de datos.

    Esta función construye y retorna la URI de la base de datos basándose en parámetros predefinidos 
    como usuario, contraseña, nombre de la base de datos, host y puerto.

    Returns:
        str: La cadena de conexión de la base de datos, creada a partir de los parámetros predefinidos.
    """
    # Usuario de la base de datos
    user = 'root'
    # Contraseña de la base de datos
    password = 'eggh-22cgFb-gBg4aH6DfFAC14edeFC6'
    # Nombre de la base de datos
    db_name = 'railway'
    # Host que hospeda la base de datos
    host = 'viaduct.proxy.rlwy.net'
    # Puerto donde está montada la base de datos
    port = 51991

    # Retorna la cadena de conexión de la base de datos en formato URI.
    return f'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}'
