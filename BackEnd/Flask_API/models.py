from flask_sqlalchemy import SQLAlchemy
#libreria para encriptar contraseñas
from passlib.hash import bycript
db=SQLAlchemy  ()
#Clase para los usuarios 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        self.password = bycript.hash(password)

    def check_password(self, password):
        return bycript.verify(password, self.password)

    def __repr__(self):
        return f'<User {self.username}>'
    