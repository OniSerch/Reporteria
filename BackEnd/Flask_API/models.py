from conexion import db, usuarios_collection
#Funcion MVC para obtener la lista de usuarios
def obtener_usuarios():
    return list(usuarios_collection.find())