class vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def mostrar_marca(self):
        print(f"Marca del vehículo: {self.marca}")


class moto(vehiculo):
    pass


mi_moto = moto("Yamaha")
mi_moto.mostrar_marca()
