from flask import Flask
from flask_cors import CORS
from Login.login import login_bp  # Importamos el blueprint definido en login.py

app = Flask(__name__, template_folder="FrontEnd/Main")
app.secret_key = "clave-secreta-muy-larga-y-segura"  # NECESARIO para usar sesiones
CORS(app)

# Registramos el blueprint de Login
app.register_blueprint(login_bp)

if __name__ == "__main__":
    app.run(debug=True)
