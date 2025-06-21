from flask import Flask, jsonify
from flask_cors import CORS
from models import obtener_usuarios

app = Flask(__name__)
CORS(app)

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    usuarios = obtener_usuarios()
    for u in usuarios:
        u["_id"] = str(u["_id"])
    return jsonify(usuarios)

if __name__ == "__main__":
    app.run(debug=True)
