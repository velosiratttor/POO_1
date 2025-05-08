"""
4. Crea una clase 'Auto' con atributos marca, modelo y año. Agrega un método que
devuelva la descripción completa del auto.
"""

import os

limpia = os.system("cls")

class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
    def marcas(self):
        self.marca = input(f"¿Cuál es su marca preferida?  ")
        
    def model(self):
        self.modelo = input(f"¿Cuál es el modelo?  ")
        
    def ant(self):
        self.año = input(f"¿De qué año?  ")
        
    def final(self):
        print(f"Su marca de aunto preferida es {self.marca.upper()}")
        print(f"Siendo el mejor modelo de este el {self.modelo.upper()}")
        print(f"Y el mejor año fue el {self.año}")
        
limpia
car = Auto("","","")

print("Calificando Marcas de Auntos")
print()
car.marcas()
car.model()
car.ant()
print()
car.final()
print()


