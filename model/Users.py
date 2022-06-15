from db.db import *

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100),unique=True)
    dni = db.Column(db.String(100))
    password = db.Column(db.String(100))
    rol= db.Column(db.String(100))
    phone = db.Column(db.Integer)

    def __init__(self, fullname, email, dni, password, rol, phone):
        self.fullname = fullname
        self.email = email
        self.dni = dni
        self.password = password
        self.rol = rol
        self.phone = phone