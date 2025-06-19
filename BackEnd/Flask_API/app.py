from flask import Flask
from flask_cors import CORS #import cors es para permitir el acceso desde otros dominios
from flask_sqlalchemy import SQLAlchemy # admitir base de datos
from config import Config # importar la configuracion de la base de datos
from models import db # importar la base de datos
from route.auth import auth_bp # importar las rutas de autenticacion

#funcion para crear la aplicacion
def create_app():
    app=Flask(__name__) 
    # Configurar la aplicacion
    app.config.from_object(Config)
    #EXTENSIONES
    CORS(app)  # Permitir CORS
    JWTManager(app)  # Manejo de los tokens
    db.init_app(app)  # Inicializar la base de datos
    #Creamos las tablas de la base de datos
    with app.app_context():
        db.create_all()  # Crear todas las tablas
    return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True,)