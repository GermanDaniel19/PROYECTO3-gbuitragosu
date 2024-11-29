from db import db
from models.producto import Producto
from models.heladeria import Heladeria
from flask import Blueprint,render_template, request, flash, jsonify
from flask_login import current_user

# from app import heladeria_mia

producto_bp = Blueprint("producto_bp", __name__,url_prefix= "/producto")
lista_productos_bp = Blueprint("lista_productos_bp",__name__,url_prefix="/api/producto/lista")

@producto_bp.route("/", methods = ["GET","POST"])
def index():
    # Producto.producto_rentable
    productos = Producto.query.all()
    heladeria = Heladeria.query.filter_by(id = 1).first()
    venta_dia: float = heladeria.venta_dia
    producto_rentable: str = heladeria.producto_mas_rentable
    
    if request.method == "GET":
        #admin
        if current_user.is_admin == True or current_user.is_employee == True:
        
            return render_template("productos.html"
                                ,productos=productos
                                ,venta_dia = venta_dia 
                                ,producto_rentable = (producto_rentable if current_user.is_admin == True else "XXX")
                                )
        #Cliente
        elif current_user.is_employee == False and current_user.is_admin == False:
            return render_template("productos.html"
                                ,productos=productos
                                ,venta_dia = "XXX"
                                ,producto_rentable = "XXX"
                                )
        #No logueado
        else:
            return render_template("noautorizado.html")
        

    else:
        #vender
        if int(request.form["opcion"]) == 1:
            if current_user != None :

                producto_operar = Producto()
                try:
                    resultado: str = producto_operar.vender(int(request.form["id_producto"]))
                    flash(resultado)
                    db.session.commit()
                except Exception as e:
                    flash(f"¡¡ Oh No !! nos hemos quedado sin {e}")
            
            else: 
                return render_template("noautorizado.html")

        #Producto rentable
        if int(request.form["opcion"]) == 2:
            if current_user.is_admin == True:
                producto_operar = Producto()
                producto_operar.producto_rentable()
                db.session.commit()
            else: 
                return render_template("noautorizado.html")

        heladeria = Heladeria.query.filter_by(id = 1).first()
        venta_dia: float = heladeria.venta_dia
        producto_rentable: str = heladeria.producto_mas_rentable
        productos = Producto.query.all()
        return render_template("productos.html"
                               ,productos=productos
                               ,venta_dia = (venta_dia  if current_user.is_admin == True or current_user.is_employee == True  else "XXX")
                               ,producto_rentable = (producto_rentable  if current_user.is_admin == True else "XXX")
                               )

@lista_productos_bp.route("/",methods = ["GET","POST"])
def lista_producto():
    productos_lista = Producto.query.all()

    if request.method == "GET":
        
        return jsonify(productos = [producto.info_json() for producto in productos_lista])
    
@lista_productos_bp.route("/<int:id>", methods = ["GET"])
def lista_producto_id(id):
    try:
        producto = Producto.query.get(id)
        return jsonify(productos = producto.info_json()),201
    except Exception as e:
        return jsonify(productos = str(e)),201
    
@lista_productos_bp.route("/<nombre>", methods = ["GET"])
def lista_producto_nombre(nombre):
    try:
        producto = Producto.query.filter_by(nombre = nombre).first()
        return jsonify(productos = producto.info_json()),201
    except Exception as e:
        return jsonify(productos = str(e)),201
    

@lista_productos_bp.route("/calorias/<int:id>", methods = ["GET"])
def lista_producto_calorias_id(id):
    try:
        producto = Producto.query.get(id)
        return jsonify(Calorias_producto = producto.calorias_producto()),201
    except Exception as e:
        return jsonify(productos = str(e)),201
    
@lista_productos_bp.route("/rentabilidad/<int:id>", methods = ["GET"])
def lista_producto_rentabilidad_id(id):
    try:
        producto = Producto.query.get(id)
        return jsonify(rentabilidad_producto = producto.rentabilidad()),201
    except Exception as e:
        return jsonify(rentabilidad_producto = str(e)),201
    
@lista_productos_bp.route("/costo/<int:id>", methods = ["GET"])
def lista_producto_costo_id(id):
    try:
        producto = Producto.query.get(id)
        return jsonify(costo = producto.costo()),201
    except Exception as e:
        return jsonify(costo = str(e)),201
    
@lista_productos_bp.route("/vender/<int:id>", methods = ["GET"])
def producto_vender_id(id):
    try:
        producto = Producto.query.get(id)
        producto.vender(id)
        db.session.commit()
        return jsonify(Estado = "Vendido exitosamente"),201
    except Exception as e:
        return jsonify(f"producto no vendido: {str(e)}")