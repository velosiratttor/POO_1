
class Saludo:
    def __init__(self, nombre):
        self.nombre = nombre

    def decir_hola(self):
        print(f"Hola, soy {self.nombre}.")

# Clase hija
class SaludoFormal(Saludo):
    pass


persona = SaludoFormal("Carlos")
persona.decir_hola()

