class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def descripcion(self):
        print(f"{self.marca} {self.modelo} ({self.año})")

auto1 = Auto("Toyota", "Corolla", 2022)
auto1.descripcion()
