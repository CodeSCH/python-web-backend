from db.db import *

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    dni = db.Column(db.String(100))
    password = db.Column(db.String(100))
    card = db.Column(db.String(100))