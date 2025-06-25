#archivo para las rutas principales de la aplicacion
from flask import Blueprint, render_template
# Importamos el Blueprint de Flask para crear rutas
main_bp = Blueprint('main', __name__)
# Define el Blueprint para las rutas principales de la aplicación
@main_bp.route('/',)
def home():
    # Renderiza la plantilla principal de la aplicación
    return render_template('Main.html')