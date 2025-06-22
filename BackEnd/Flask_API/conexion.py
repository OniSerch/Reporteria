import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Cargar .env archivo
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# Conectar a MongoDB
MONGO_URI = os.getenv("MONGO_URI")
print("MONGO_URI:", MONGO_URI)
# Crear cliente de MongoDB
client = MongoClient(MONGO_URI)
db = client["Reporteria"]
# Seleccionar la colección de usuarios
usuarios_collection = db["Usuarios"]

# Verificación (solo si corres este archivo directamente)
if __name__ == "__main__":
    print("Bases de datos:", client.list_database_names())
    print("Colecciones:", db.list_collection_names())