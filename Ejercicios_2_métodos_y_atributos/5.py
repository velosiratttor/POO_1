class animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def decir_nombre(self):
        print(f"Me llamo {self.nombre}")


class gato(animal):
    pass


gatito = gato("Michi")
gatito.decir_nombre()
