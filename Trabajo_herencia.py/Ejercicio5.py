#Crea una clase 'Animal' con el atributo 'nombre' y un método que diga su nombre. Luego crea una clase 'Gato' 
#que herede esos elementos.

class Animal:
    def __init__(self, nombre):  # Constructor con __init__
        self.nombre = nombre

    def decir_nombre(self):
        print(f"Me llamo {self.nombre}")

class Gato(Animal):  # Hereda de Animal
    def __init__(self, nombre):  # También usa el constructor __init__
        super().__init__(nombre)  # Llama al constructor de la clase padre

# Ejemplo de uso
mi_gato = Gato("Michi")
mi_gato.decir_nombre()

