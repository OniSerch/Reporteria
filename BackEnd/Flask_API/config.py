from pymongo import MongoClient
class config:
    # Database configuration
    client=MongoClient('mongodb+srv://sergiojairceron:<db_password>@cluster0.03zbm47.mongodb.net/')  # MongoDB connection string
    db=client['reporteria']  # Nombre de la base de datos
    collection=db['users']  # Coleccion de usuarios
    DEBUG = True  # Activa el modo de depuración
    TESTING = False  # Desactivar pruebas
    CSRF_ENABLED = True  # Prender proteccion CSRF
    SECRET_KEY = 'your_secret_key_here' 
    # JWT configuration
    JWT_SECRET = 'your_jwt_secret_here'  # Token secreto para JWT
    JWT_ALGORITHM = 'HS256'  # Algoritmo de firma del JWT
    JWT_EXPIRATION_DELTA = 3600  # Exoniracion del token en segundos (1 hora)
    JWT_ISSUER = 'reporteria'  # para jtokens emitidos por Reporteria
    JWT_AUDIENCE = 'reporteria_users'  # audiencia del token para usuarios de Reporteria 
    JWT_LEEWAY = 10  # tiempo de gracia para la expiracion del token en segundos