import os  # Importa el módulo os para manejar variables de entorno
from dotenv import load_dotenv  # Importa dotenv para cargar variables de entorno desde un archivo .env
# Cargar las variables de entorno desde el archivo .env
from pymongo import MongoClient

#Buenas practicas se mueve al env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__),'..','env'))
class config:
    # Database configuration
    MONGO_URI=os.getenv("MONGO_URI")
    
    
    
    client=MongoClient('mongodb+srv://sergiojairceron:<1l1KR3S4W1>@cluster0.03zbm47.mongodb.net/')  # MongoDB connection string
    db=client['Reporteria']  # Nombre de la base de datos
    collection=db['usuarios']  # Coleccion de usuarios
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