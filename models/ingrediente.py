from db import db

class Ingrediente(db.Model):
    __tablename__ = "ingredientes"
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    nombre = db.Column(db.String(50), nullable = False)
    contador = db.Column(db.Float, nullable = False)
    calorias = db.Column(db.Integer, nullable = False)
    precio = db.Column(db.Float, nullable = False)
    vegetariano = db.Column(db.Integer, nullable = False)
    sabor = db.Column(db.String(50), nullable = True)
    is_complemento = db.Column(db.Boolean, nullable = True)
    

    def es_sano(self,id_ingrediente) -> str:
        ingrediente_consultar = Ingrediente.query\
            .filter_by(id = id_ingrediente)\
            .first()
        
        resultado: str = "no se encuentra el ingrediente"
        
        if isinstance(ingrediente_consultar,Ingrediente):
                if ingrediente_consultar.calorias < 100 \
                    or ingrediente_consultar.vegetariano == True:

                    resultado = (f"Ingrediente {ingrediente_consultar.nombre} es SANO !!!")
                
                else: 
                    resultado = (f"Ingrediente {ingrediente_consultar.nombre} NO es sano")
            
        return resultado

    def bajar_complemento(self,id_ingrediente: int) -> str:

        ingrediente_consultar = Ingrediente.query\
            .filter_by(id = id_ingrediente, is_complemento = True )\
                .first()
        
        resultado: str = "Producto no existe o no es complemento"

        if isinstance(ingrediente_consultar,Ingrediente):
            ingrediente_consultar.contador = 0.0
            # db.session.commit()
            resultado = f"Ingrediente {ingrediente_consultar.nombre} actualizado exitosamente"

        return resultado

    def reabastecer(self, id_ingrediente: int) -> str:
        
        ingrediente_consultar = Ingrediente.query\
            .filter_by(id = id_ingrediente)\
            .first()
        
        resultado: str = "Producto no existe"

        if isinstance(ingrediente_consultar, Ingrediente):
             
            if ingrediente_consultar.is_complemento == True:
                ingrediente_consultar.contador +=10
            else:
                ingrediente_consultar.contador +=5

            resultado = f"Ingrediente {ingrediente_consultar.nombre} actualizado con exito"
        
        return resultado
    
    def info_json(self) -> str:
        return {
            "id" : self.id
            ,"nombre" : self.nombre
            ,"contador" : self.contador
            ,"calorias"  : self.calorias
            ,"precio" : self.precio
            ,"vegetariano" : self.vegetariano
            ,"sabor" : self.sabor
            ,"is_complemento" : self.is_complemento
        }