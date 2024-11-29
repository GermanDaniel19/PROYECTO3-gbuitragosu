# from db import db
from models.ingrediente import Ingrediente
from flask import Blueprint,render_template, request, flash, jsonify
from flask_login import current_user, login_required

from db import db


ingrediente_bp = Blueprint("ingrediente_bp",__name__,url_prefix="/ingredientes")
lista_ingredientes_bp = Blueprint("lista_ingredientes_bp",__name__,url_prefix="/api/ingredientes/lista")

@ingrediente_bp.route("/", methods = ["GET","POST"])
@login_required
def index():
    
    ingredientes = Ingrediente.query.all()
    if request.method == "GET":
        if current_user.is_admin == True or current_user.is_employee == True:
            return render_template("ingredientes.html", ingredientes = ingredientes)
        else:
            return render_template("noautorizado.html")
    else:
        if int(request.form["opcion"]) == 1:

            if current_user.is_admin == True or  current_user.is_employee == True:
                ingrediente_consultar = Ingrediente()
                resultado: str = ingrediente_consultar.es_sano(int(request.form["id_ingrediente"]))
                flash(resultado)
    
            # return render_template("ingredientes.html", ingredientes = ingredientes)
            else:
                return render_template("noautorizado.html")
        #Bajar complemento a 0
        elif int(request.form["opcion"]) == 3:
            
            if current_user.is_admin == True or  current_user.is_employee == True:

                ingrediente_consultar = Ingrediente()

                resultado: str = ingrediente_consultar\
                    .bajar_complemento(int(request.form["id_ingrediente"]))
                
                db.session.commit()
                flash(resultado)
            else:
                return render_template("noautorizado.html")

            # return render_template("ingredientes.html", ingredientes = ingredientes)
        
        #Reabastecer
        elif int(request.form["opcion"]) == 2:

            if current_user.is_admin == True or  current_user.is_employee == True:
            
                ingrediente_consultar = Ingrediente()
                resultado: str = ingrediente_consultar\
                    .reabastecer(int(request.form["id_ingrediente"]))
                
                flash(resultado)
                db.session.commit()     

            else:
                return render_template("noautorizado.html")
        #     return render_template("ingredientes.html",ingredientes = ingredientes)
        
        # else: 
        return render_template("ingredientes.html",ingredientes = ingredientes)

@lista_ingredientes_bp.route("/", methods = ["GET","POST"])
def lista_ingredientes():
    ingredientes_lista = Ingrediente.query.all()

    return jsonify(ingredientes = [ingrediente.info_json() for ingrediente in ingredientes_lista])

@lista_ingredientes_bp.route("/<int:id>")
def lista_ingredientes_id(id):
    ingredientes_lista = Ingrediente.query.get(id)
    return jsonify(ingrediente = ingredientes_lista.info_json())

@lista_ingredientes_bp.route("/<nombre>")
def lista_ingredientes_nombre(nombre):
    ingredientes_lista = Ingrediente.query.filter_by(nombre = nombre).first()
    return jsonify(ingrediente = ingredientes_lista.info_json())

@lista_ingredientes_bp.route("/es_sano_id/<int:id>")
def es_sano_id(id):
    ingredientes_lista = Ingrediente.query.get(id)
    return jsonify(es_sano = ingredientes_lista.es_sano(id))

@lista_ingredientes_bp.route("/reabastecer/<int:id>")
def reabastecer_id(id):
    ingredientes_lista = Ingrediente.query.get(id)
    return jsonify(reabastecer = ingredientes_lista.reabastecer(id))

@lista_ingredientes_bp.route("/renovar/<int:id>")
def renovar_id(id):
    ingredientes_lista = Ingrediente.query.get(id)
    return jsonify(renovar = ingredientes_lista.bajar_complemento(id))