#AGREGAR 3 METODOS MAS A ANIMAL Y CREAR 3 NUEVAS CLASES HIJAS 
#QUE HEREDEN DE LA CLASE PADRE "ANIMAL" CON METODOS PROPIOS DE ELLAS

# Clase base
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido.")

    
    def moverse(self):
        print(f"{self.nombre} se está moviendo.")

    def info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad} años.")

    def esta_vivo(self):
        print(f"{self.nombre} está vivo y saludable.")


# Clases hijas
class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} está ladrando: ¡Guau guau!")

class Gato(Animal):
    def maullar(self):
        print(f"{self.nombre} está maullando: ¡Miau!")

class Pajaro(Animal):
    def volar(self):
        print(f"{self.nombre} está volando por el cielo.")


# Ejemplo de uso
perro = Perro("Firulais", 5)
perro.comer()
perro.ladrar()
perro.info()

gato = Gato("Michi", 3)
gato.dormir()
gato.maullar()
gato.esta_vivo()

pajaro = Pajaro("Piolín", 1)
pajaro.hacer_sonido()
pajaro.volar()
pajaro.moverse()

