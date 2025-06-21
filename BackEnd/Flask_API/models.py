from conexion import db, usuarios_collection

def obtener_usuarios():
    return list(usuarios_collection.find())