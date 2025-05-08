#Crea una clase 'Estudiante' que almacene el nombre, edad y promedio. Agrega un método que indique si el estudiante
# está aprobado (promedio >= 60). 

class Estudiante:
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    def mostrar(self):
        print("Nombre del estudiante:", self.nombre)
        print("Edad:", self.edad)
        print("Promedio:", self.promedio)
        if self.promedio >= 60:
            print("Estado: Aprobado")
        else:
            print("Estado: Reprobado")

nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
promedio = float(input("Ingrese el promedio del estudiante: "))

est = Estudiante(nombre, edad, promedio)
est.mostrar()
