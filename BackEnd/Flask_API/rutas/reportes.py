from flask import Blueprint, request, jsonify

reportes_bp = Blueprint('reportes', __name__)

@reportes_bp.route('/')
def ver_reportes():
    # aquí podrías validar que haya un token o sesión
    # por ahora simulamos restricción
    autorizado = request.headers.get("Authorization")
    if autorizado != "Token123":
        return jsonify({"error": "No autorizado"}), 401

    return jsonify({"mensaje": "Contenido de reportes confidenciales"})

