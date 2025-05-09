#Haz una clase 'Persona' con los atributos 'nombre' y 'edad', y un método para presentarse. Luego crea una clase 
#Profesor' que herede de 'Persona'.

class Persona :
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def decir(self):
        print(f"Mi nombre es: {self.nombre} y tengo {self.edad}")

class Profesor(Persona):
    def __init__(self, nombre,edad):
        super().__init__(nombre, edad)
        
Profesor1 = Profesor("Samuel",20)
Profesor1.decir()