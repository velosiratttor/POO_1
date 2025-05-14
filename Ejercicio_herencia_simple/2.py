#Una empresa tiene una flota de vehículos. 
# Diseña una clase Vehiculo con atributos marca y modelo, 
# y un método para encender el vehículo. Después, crea una 
# clase Motocicleta que herede de Vehiculo y agregue el atributo 
# cilindraje. Implementa un método que imprima todos los datos de la motocicleta.
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def encender(self):
        print(f"El vehículo {self.marca} {self.modelo} está encendido.")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje

    def mostrar_datos(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Cilindraje: {self.cilindraje}cc")


marca = input("Marca de la motocicleta: ")
modelo = input("Modelo: ")
cilindraje = int(input("Cilindraje (cc): "))

moto = Motocicleta(marca, modelo, cilindraje)
moto.encender()
moto.mostrar_datos()

