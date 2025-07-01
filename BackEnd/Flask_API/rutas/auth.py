import datetime
from flask import Blueprint, request, jsonify
from ..conexion import usuarios_collection
from Flask_API.utils.hash import hash, verificar
from Flask_API.utils.hash import hash
from Flask_API.utils.brainfuck import to_brainfuck

auth_bp = Blueprint('auth', __name__)
@auth_bp.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()

    # Verificar si ya existe
    if usuarios_collection.find_one({"email": data["email"]}):
        return jsonify({"Mensaje": "El correo electrónico ya está registrado"}), 409

    hashed = hash(data["password"])
    brain_hash = to_brainfuck(hashed)

    nuevo_usuario = {
        "usuario": data["usuario"],
        "email": data["email"],
        "pass_hash": brain_hash,
        "rol": "normal",
        "pago": False,
        "activo": True,
        "logueo": {
            "fecha": datetime.utcnow().isoformat() + "Z",
            "conteo": 0
        },
        "plan": {
            "nombre": "Free",
            "fecha_inicio": None,
            "fecha_fin": None
        }
    }

    usuarios_collection.insert_one(nuevo_usuario)

    return jsonify({
        "Mensaje": "Registro exitoso",
        "Hash": hashed
    }), 201







@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    data = request.get_json()
    usuario = usuarios_collection.find_one({"email": data['email']})

    if not usuario:
        return jsonify({"Mensaje": "Usuario no encontrado"}), 404

    if not verificar(data['password'], usuario['pass_hash']):
        return jsonify({"Mensaje": "Contraseña incorrecta"}), 401

    # Verificar expiración si es premium
    if usuario['rol'] == 'premium':
        fecha_fin = usuario["plan"].get("fecha_fin")
        if fecha_fin and datetime.utcnow() > fecha_fin:
            usuarios_collection.update_one(
                {"_id": usuario["_id"]},
                {"$set": {"rol": "normal", "pago": False}}
            )
            usuario["rol"] = "normal"

    return jsonify({
        "Mensaje": "Inicio de sesión exitoso",
        "Usuario": usuario['usuario'],
        "Rol": usuario['rol'],
        "Plan": usuario['plan']  # ⬅ lo agregas aquí
    }), 200