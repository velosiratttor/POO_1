#10. Implementa una clase 'Empleado' con nombre y salario. Agrega un método para calcular el salario anual.

class Empleado:
    
    def __init__(self, nombre , salario):
        self.nombre = nombre
        self.salario = salario
    
    def calculo_salario_anual(self):
        return self.salario * 12

empleado1 = Empleado(nombre='Miguel',salario=10000)
print(empleado1.calculo_salario_anual())
        