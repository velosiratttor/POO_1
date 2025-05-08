#Implementa una clase 'Empleado' con nombre y salario. Agrega un método para calcular el salario anual

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario  

    def calcular_salario_anual(self):
        salario_anual = self.salario * 12
        print(f"Empleado: {self.nombre}")
        print(f"Salario mensual: {self.salario:.2f}")
        print(f"Salario anual: {salario_anual:.2f}")

# Ejemplo de uso
nombre = input("Ingrese el nombre del empleado: ")
salario = float(input("Ingrese el salario mensual: "))

empleado = Empleado(nombre, salario)
empleado.calcular_salario_anual()
