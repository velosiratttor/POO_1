class Calculadora:
    def sumar(self, a, b):
        print("Suma:", a + b)

    def restar(self, a, b):
        print("Resta:", a - b)

    def multiplicar(self, a, b):
        print("Multiplicación:", a * b)

    def dividir(self, a, b):
        if b != 0:
            print("División:", a / b)
        else:
            print("Error: División por cero")

calc = Calculadora()
calc.sumar(4, 3)
calc.dividir(10, 3)
calc.multiplicar(6,7)
