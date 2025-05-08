#Diseña una clase 'Círculo' que tenga un atributo radio y métodos para calcular el área y el perímetro.

class Circulo:
    def __init__(self, radio):
        self.radio = radio 

    def calcular_area(self):
        pi = 3.1416
        return pi * (self.radio ** 2)

    def calcular_perimetro(self):
        pi = 3.1416
        return 2 * pi * self.radio
    
mi_circulo = Circulo(3)

# Mostrar resultados
print("Área:", mi_circulo.calcular_area())
print("Perímetro:", mi_circulo.calcular_perimetro())
