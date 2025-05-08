"""1. Crea una clase llamada 'Persona' con los atributos nombre y edad. Agrega un
método que imprima un saludo con el nombre."""

import time
import os


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludo(self):
        print(f"Hola {self.nombre}")
        print(f"¿Tienes {self.edad} años?")
        
saludo_1 = Persona("Juan",25)
saludo_2 = Persona("Carla",20)
saludo_3 = Persona("María",25)

saludo_1.saludo()
saludo_2.saludo()
saludo_3.saludo()

print("Fin del programa")
print("Espera 5 segundos ...")
time.sleep(5)
os.system("cls")
