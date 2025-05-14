#Una empresa necesita manejar información básica de sus empleados. 
#Crea una clase Empleado con los atributos nombre y salario, y un método para
#mostrar esta información. Luego, crea una clase Gerente que herede de Empleado
#y agregue el atributo departamento.
#Implementa una función que permita mostrar toda la información del gerente.

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Salario: {self.salario}")

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Departamento: {self.departamento}")

# Ejemplo
g = Gerente("Ana", 5000, "Recursos Humanos")
g.mostrar_info()

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Salario: {self.salario}")

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Departamento: {self.departamento}")


nombre = input("Nombre del gerente: ")
salario = float(input("Salario: "))
departamento = input("Departamento: ")

gerente = Gerente(nombre, salario, departamento)
gerente.mostrar_info()
