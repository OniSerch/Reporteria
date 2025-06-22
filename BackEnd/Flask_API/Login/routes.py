from flask import Blueprint, render_template, jsonify
from models import obtener_usuarios

# Blueprint llamado login
login_bp = Blueprint('login', __name__, template_folder='../../FrontEnd/Main')

# Ruta raíz que muestra la vista de login
@login_bp.route("/")
def index():
    return render_template("Main.html")

# Ruta API para obtener usuarios
@login_bp.route("/usuarios", methods=["GET"])
def listar_usuarios():
    usuarios = obtener_usuarios()
    for u in usuarios:
        u["_id"] = str(u["_id"])
    return jsonify(usuarios)
