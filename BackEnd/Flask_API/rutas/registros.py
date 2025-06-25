#Aplicacion para la gestion de registros de usuarios
from flask import Blueprint, render_template

# Importamos el Blueprint de Flask para crear rutas
registros_bp = Blueprint('registros', __name__)
@registros_bp.route('/login')
def login():
    # Renderiza la plantilla de inicio de sesión
    return render_template('Login.html')

@registros_bp.route('/registro')
def registro():
    return render_template('Registro.html')