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
    usuarios_collection.insert_one({
        "email": data['email'],
        "password": hashed,
        "nombre": data.get('nombre', ''),
        "apellido": data.get('apellido', '')
    })
    brainfuck_hash = to_brainfuck(hashed)
    return jsonify({
        "Mensaje": "Registro exitoso",
        "Hash": hashed,
        "Brainfuck": brainfuck_hash
    }), 201
