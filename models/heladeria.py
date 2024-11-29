from db import db

class Heladeria(db.Model):
    __tablename__ = "heladeria"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    producto_mas_rentable = db.Column(db.String(100), nullable = True)
    venta_dia = db.Column(db.Float, nullable = False)