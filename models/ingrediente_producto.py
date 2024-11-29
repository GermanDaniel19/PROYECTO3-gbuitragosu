from db import db

ingredientes_productos = db.Table(
    'ingredientes_productos',
    # id = db.Column(db.Integer, primary_key = True),
    db.Column("id_producto", db.Integer, db.ForeignKey("productos.id_producto")),
    db.Column("id_ingrediente", db.Integer, db.ForeignKey("ingredientes.id"))
    )