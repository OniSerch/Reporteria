from pymongo import MongoClient

# URI y nombre de la base de datos
MONGO_URI = 'mongodb+srv://sergiojairceron:1l1KR3S4W1@cluster0.03zbm47.mongodb.net/'
MONGO_DB = 'Reporteria'

def dbConexion():
    try:
        # Crear cliente y hacer ping para verificar conexión
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        client.admin.command('ping')

        db = client[MONGO_DB]
        print("✅ Conectado a la BD correctamente")

        # Prueba: listar colecciones disponibles
        colecciones = db.list_collection_names()
        print("📂 Colecciones disponibles en la BD:")
        for col in colecciones:
            print(f"  - {col}")

        return db
    except Exception as e:
        print(f"❌ Error al conectarse: {e}")
        return None

# Ejecutar si este archivo es el principal
if __name__ == "__main__":
    dbConexion()
from pymongo import MongoClient
