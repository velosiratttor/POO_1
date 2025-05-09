# Crea una clase 'Vehiculo' con el atributo 'marca' y un método que muestre la marca. Luego una clase 'Moto' 
#que herede eso

class Vehiculo:
    def __init__(self,marca):
        self.marca = marca
        
    def metodo(self):
        print(f"La marca es {self.marca}")
        
class Moto(Vehiculo):
    def __init__(self, marca):
        super().__init__(marca)
        
marca1 = Moto("Zuzuki")
marca1.metodo()

