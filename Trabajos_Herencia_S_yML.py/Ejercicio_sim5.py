#                               Registro Académico
#En una universidad, desarrolla una clase Persona con atributos nombre y edad. Luego, crea una clase Estudiante que
#herede de Persona y agregue un atributo carrera. Implementa un método que imprima todos los datos del estudiante

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
class Estudiante(Persona):
    def __init__(self, nombre, edad,carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        
    def Uni(self):
        print(f"El nombre del estudiante {self.nombre}, y la edad {self.edad} años y la carrear que eligio {self.carrera}")
        
universidad = Estudiante("Samuel",20,"Ingeneria en computación")

universidad.Uni()