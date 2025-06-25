from flask import Flask
from flask_cors import CORS

app = Flask(__name__, template_folder="../../FrontEnd/Main")
CORS(app)

from .rutas.main import main_bp
from .rutas.auth import auth_bp
from .rutas.registros import registros_bp
from .rutas.reportes import reportes_bp

app.register_blueprint(main_bp)
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(registros_bp)
app.register_blueprint(reportes_bp, url_prefix="/reportes")
