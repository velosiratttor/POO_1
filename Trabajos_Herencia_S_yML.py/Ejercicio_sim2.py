#2. Gestión de Vehículos en una Empresa de Transporte

#Una empresa tiene una flota de vehículos. Diseña una clase Vehiculo con atributos marca y modelo, y un método para 
# encender el vehículo. Después, crea una clase Motocicleta que herede de Vehiculo y agregue el atributo cilindraje.
# Implementa un método que imprima todos los datos de la motocicleta.

class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        
    def Encender_Vehiculo(self):
        print(f"La marca del Vehiculo es: {self.marca} y el modelo es: {self.modelo}")
        
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo,cilindraje):
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje
        print(f"El cilindraje es: {self.cilindraje}")
        
trasporte = Motocicleta("Zuzuki","Gixer250",200)

trasporte.Encender_Vehiculo()