class Animal:
    def hablar(self):
        print("Este animal hace un sonido.")

class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau!")

class Vaca(Animal):
    def hablar(self):
        print("Muuu")
animal1 = Perro()
animal2 = Gato()
animal3= Vaca()
animal1.hablar()
animal2.hablar()
animal3.hablar()