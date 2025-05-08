#Crea una clase 'Animal' con un método 'hablar()' que sea sobrescrito por clases hijas como 'Perro' y 'Gato'. 

class Animal:
    def hablar(self):
        return "Este animal hace un sonido."

class Perro(Animal):
    def hablar(self):
        return "Guau"

class Gato(Animal):
    def hablar(self):
        return "Miau"

# Ejemplo de uso:
animales = [Perro(), Gato(), Animal()]
for animal in animales:
    print(animal.hablar())
