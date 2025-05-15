#Crear una clase `Empleado` con atributos como nombre, ID y salario, con un método para 
#calcular bonificaciones anuales.
class Empleado:
    def __init__(self, nombre, id_empleado, salario):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.salario = salario

    def calcular_bonificacion(self, porcentaje):
        return self.salario * porcentaje / 100


e = Empleado("Ana", "E123", 50000)
print(e.calcular_bonificacion(10)) 
