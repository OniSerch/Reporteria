import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, session

# Ruta absoluta para encontrar correctamente el HTML desde cualquier lugar
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../FrontEnd/Main'))
login_bp = Blueprint('login', __name__, template_folder=template_dir)

# Simulamos base de datos de usuarios (esto deberías reemplazarlo con conexión real)
usuarios_mock = {
    "admin@colektia.com": "123456",  # correo: contraseña
    "sergio@colektia.com": "qwerty"
}

@login_bp.route("/")
def mostrar_login():
    return render_template("Main.html")

@login_bp.route("/login", methods=["POST"])
def procesar_login():
    email = request.form.get("email")
    password = request.form.get("password")

    # Validación simple (deberías usar una base de datos real)
    if email in usuarios_mock and usuarios_mock[email] == password:
        session["usuario"] = email
        return redirect(url_for("login.dashboard"))
    else:
        flash("Credenciales inválidas")
        return redirect(url_for("login.mostrar_login"))

@login_bp.route("/dashboard")
def dashboard():
    if "usuario" in session:
        return f"Bienvenido, {session['usuario']}"
    else:
        return redirect(url_for("login.mostrar_login"))

@login_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login.mostrar_login"))
