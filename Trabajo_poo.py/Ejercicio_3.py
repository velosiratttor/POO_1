# Implementa una clase 'Calculadora' con métodos para sumar, restar, multiplicar y dividir dos números.

class calculadora:
    def __init__(self,sumar):
        self.sumar = sumar 
        
    def sumar_1(self):
        sumar = 2
        return sumar + (self.sumar)
    
    def restar_1(self):
        restar = 2
        return restar - (self.sumar)
    
    def multiplicar_1(self):
        multiplicar = 2
        return multiplicar * (self.sumar)
    
    def dividir_1(self):
        dividir = 2
        return dividir / (self.sumar)
    
my_calculadora = calculadora(20)

print("La suma de 2 es,", my_calculadora.sumar_1())
print("La multiplicacion es,", my_calculadora.multiplicar_1())