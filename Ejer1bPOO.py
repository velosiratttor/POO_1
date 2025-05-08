"""2. Diseña una clase 'Círculo' que tenga un atributo radio y métodos para calcular el
área y el perímetro.         A = π r² y c = 2 π r 
"""
import math
import os
limpia = os.system("cls")
pi = math.pi

class Circulo:
    def __init__(self, radio=0, area=0, peri=0):
        self.radio = radio
        self.area = area
        self.peri = peri
        
    def radios(self):
        self.radio = float(input("Ingrese el valor del radio: "))
    
    def areas(self):
        self.area = pi * (self.radio ** 2)
        
    def peris(self):
        self.peri = 2 * pi * self.radio
        
limpia
print()
circ = Circulo()

circ.radios()
circ.areas()
circ.peris()

print()
print(f"El radio del Círculo es: {circ.radio}")
print()
print(f"El área del Círculo es: {round(circ.area,5)}")
print()
print(f"Y su Perímetro es: {round(circ.peri,5)}")
print()