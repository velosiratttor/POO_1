#10. Implementa una clase 'Empleado' con nombre y salario. Agrega un método para calcular el salario anual.

class Empleado:
    def __init__(self, nombre, salario_mensual):
        self.nombre = nombre
        self.salario_mensual = salario_mensual

    def calcular_salario_anual(self): 
        salario_anual = self.salario_mensual * 12
        return salario_anual

empleado1 = Empleado("Ana Pérez", 2500.00)
salario_anual_ana = empleado1.calcular_salario_anual()
print(f"El salario anual de {empleado1.nombre} es: ${salario_anual_ana:.2f}")

empleado2 = Empleado("Carlos López", 3200.50)
salario_anual_carlos = empleado2.calcular_salario_anual()
print(f"El salario anual de {empleado2.nombre} es: ${salario_anual_carlos:.2f}")