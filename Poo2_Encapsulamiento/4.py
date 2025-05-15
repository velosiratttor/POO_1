#Haz una clase Proveedor con nombre y número de 
#entregas realizadas. Usa  encapsulamiento para 
#que las entregas solo puedan incrementarse 
# desde un  método, evitando cambios arbitrarios. 
class Proveedor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__entregas = 5

    @property
    def entregas(self):
        return self.__entregas

    def registrar_entrega(self):
        self.__entregas += 1

proveedor = Proveedor("Transportes XYZ")
proveedor.registrar_entrega()
proveedor.registrar_entrega()
print(proveedor.entregas)
