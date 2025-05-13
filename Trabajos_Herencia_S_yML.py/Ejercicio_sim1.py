# Sistema de Recursos Humanos

# Una empresa necesita manejar información básica de sus empleados. Crea una clase Empleado con los atributos nombre 
# y salario, y un método para mostrar esta información. Luego, crea una clase Gerente que herede de Empleado y 
# agregue el atributo departamento. Implementa una función que permita mostrar toda la información del gerente.

class Empleado:
    def __init__(self,nombre,salario):
        self.nombre = nombre
        self.salario = salario
        
    def mostrar_informacion(self):
        print(f"Mi nombre es: {self.nombre} y mi salario es de: {self.salario}")

class Gerente(Empleado):
        def __init__(self, nombre,salario,departamento):
            super().__init__(nombre, salario)
            self.departamento = departamento
            print(f"Mi departamento es: {self.departamento}")
            
sistema = Gerente("Samuel",20000,"Managua")

sistema.mostrar_informacion()