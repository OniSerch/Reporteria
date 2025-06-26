from flask import Blueprint, request, jsonify
from ..conexion import usuarios_collection
from Flask_API.utils.hash import hash, verificar
from Flask_API.utils.hash import hash
from Flask_API.utils.brainfuck import to_brainfuck

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    if usuarios_collection.find_one({"email": data['email']}):
        return jsonify({"Mensaje": "El correo electrónico ya está registrado"}), 409
   
    hashed = hash(data['password'])
    pago_estado = data.get('pago', False)  # opcional en el JSON
    rol = "premium" if pago_estado else "normal"
    brainfuck_hash = to_brainfuck(hashed)
   
    usuarios_collection.insert_one({
        "Usuario": data['usuario'],
        "PassHash": brainfuck_hash,
        "Correo": data['email'],
        "Rol": rol,
        "Plan":{},
        "Logueo":None,
        "Activo": True,
        "Pago": pago_estado,
    })
    brainfuck_hash = to_brainfuck(hashed)
    return jsonify({
        "Mensaje": "Registro exitoso",
        "Hash": hashed,
        "Brainfuck": brainfuck_hash
    }), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = usuarios_collection.find_one({"Correo": data['email']})
    if not usuario:
        return jsonify({"Mensaje": "Usuario no encontrado"}), 404
    if not verificar(data['password'], usuario['PassHash']):
        return jsonify({"Mensaje": "Contraseña incorrecta"}), 401
    return jsonify({
        "Mensaje": "Inicio de sesión exitoso",
        "Usuario": usuario['Usuario'],
        "Rol": usuario['Rol']
    }), 200