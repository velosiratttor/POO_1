#12. Crea una clase 'Animal' con un método 'hablar()' que sea sobrescrito por clases hijas como 'Perro' y 'Gato'.

class Animal:
    def hablar(self):
        print("El animal hace un sonido.")

class Perro(Animal):
    def hablar(self):
        print("¡Guau! ¡Guau!")

class Gato(Animal):
    def hablar(self):
        print("¡Miau! ¡Miau!")

mi_perro = Perro()
mi_perro.hablar()        

mi_gato = Gato()
mi_gato.hablar()        

def hacer_hablar(animal):
    animal.hablar()

hacer_hablar(mi_perro)        
hacer_hablar(mi_gato)        