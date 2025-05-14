#En una universidad, desarrolla una clase Persona 
# con atributos nombre y edad. Luego, crea una clase 
# Estudiante que herede de Persona y agregue un atributo carrera. 
# Implementa un método que imprima todos los datos del estudiante.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}")

# Integración con teclado
nombre = input("Nombre del estudiante: ")
edad = int(input("Edad: "))
carrera = input("Carrera universitaria: ")

estudiante = Estudiante(nombre, edad, carrera)
estudiante.mostrar_datos()
