class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def salario_anual(self):
        print("Salario anual:", self.salario * 12)

empleado = Empleado("Chester", 2500)
empleado.salario_anual()
