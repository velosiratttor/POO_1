# Clase base
class Matematica:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def multiplicar(self):
        resultado = self.numero1 * self.numero2
        print(f"La multiplicación de {self.numero1} x {self.numero2} es {resultado}")

class EjerciciosMatematicos(Matematica):
    pass


ejercicio = EjerciciosMatematicos(6, 9)
ejercicio.multiplicar()

