#archivo para las rutas principales de la aplicacion manejo de datos de los htmls
from flask import Blueprint, render_template, request, jsonify
from ..conexion import usuarios_collection

# Importamos el Blueprint de Flask para crear rutas
auth_bp = Blueprint('auth', __name__)

# Define el Blueprint para las rutas de autenticación de la aplicación
@auth_bp.route('/login', methods=['POST'])
#define la ruta de inicio de sesión
def login():
    # Maneja la solicitud de inicio de sesión
    data= request.get_json()
    # Verifica si se proporcionó el correo electrónico y la contraseña
    usuario=usuarios_collection.find_one({"email": data['email']})
    #Si el usuario existe y la contraseña coincide, devuelve un mensaje de éxito
    if usuario and usuario['password'] == data['password']:
        return jsonify({"Mensaje": "Login exitoso"})
    #en caso contrario, devuelve un mensaje de error
    return jsonify({"Mensaje": "Credenciales inválidas"}), 401

# Define la ruta para el registro de usuarios
@auth_bp.route('/registro', methods=['POST'])
def registro():
    # Maneja la solicitud de registro de usuario
    data = request.get_json()
    # Verifica si el correo electrónico ya está registrado
    if usuarios_collection.find_one({"email": data['email']}):
        return jsonify({"Mensaje": "El correo electrónico ya está registrado"}), 409
    usuarios_collection.insert_one(
        {
            "email": data['email'],
            "password": data['password'],
            "nombre": data.get('nombre', ''),
            "apellido": data.get('apellido', '')
        }
    )
    return jsonify({"Mensaje": "Registro exitoso"}), 201