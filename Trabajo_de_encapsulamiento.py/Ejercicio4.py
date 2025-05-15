#                                Proveedor y Entregas 
#Haz una clase Proveedor con nombre y número de entregas realizadas. Usa
#encapsulamiento para que las entregas solo puedan incrementarse desde un
#método, evitando cambios arbitrarios. 

class Proveedor:
    def __init__(self,nombre,numero_de_entregas):
        self.nombre = nombre #Public
        self.__numero_de_entrega = numero_de_entregas #privado
        
    def mostrar(self,cantidad = 1): 
        if cantidad == 1:
            self.__numero_de_entrega += 1
            print("La cantida es: ",self.__numero_de_entrega)
        else:
            print("La cantidad es invalidad")
entregas = Proveedor("Sammuel",10)
print(entregas.nombre)
entregas.mostrar(1)

