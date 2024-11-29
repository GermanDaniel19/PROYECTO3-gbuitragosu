
def es_sano(calorias:int, es_vegetariano:bool) -> bool:
    if calorias < 100 or es_vegetariano is True:
        return True
    else:
        return False


def conteo_calorias(calorias:list) -> float:
    calorias_totales:int = 0
    for caloria in calorias:
        calorias_totales += caloria

    return round(calorias_totales,2)

def costo(precio1:float , precio2:float , precio3:float ) -> float:
    return precio1 + precio2 + precio3

def rentabilidad(precio:float, precio1:float , precio2:float , precio3:float) -> float:
    return precio-costo(precio1 , precio2 , precio3)

def mejor_producto(producto1:dict, producto2:dict, producto3:dict, producto4:dict) -> str:
    nombre_producto:str = producto1["nombre"]
    rentabilidad:float = producto1["rentabilidad"]

    productos:list = [producto2, producto3, producto4]

    for producto in productos:
        if producto["rentabilidad"] > rentabilidad:
            rentabilidad = producto["rentabilidad"]
            nombre_producto = producto["nombre"]

    return nombre_producto


# print(es_sano(321,True))
# print(conteo_calorias({100,900}))

ingrediente1:dict = {"nombre": "Helado de Fresa", "precio": 1200}
ingrediente2:dict = {"nombre": "Chispas de chocolate", "precio": 500}
ingrediente3:dict = {"nombre": "Mani Japonés", "precio": 900}
# print(costo(ingrediente1, ingrediente2, ingrediente3))

# print(rentabilidad(7500,ingrediente1, ingrediente2, ingrediente3))

producto1:dict = {"nombre": "Samurai de fresas", "rentabilidad": 4900}
producto2:dict = {"nombre": "Samurai de mandarinas", "rentabilidad": 2500}
producto3:dict = {"nombre": "Malteda chocoespacial", "rentabilidad": 11000}
producto4:dict = {"nombre": "Cupihelado", "rentabilidad": 3200}

print(mejor_producto(producto1, producto2, producto3, producto4))


