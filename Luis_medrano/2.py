
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        print("Área:", 3.1415 * self.radio ** 2)

    def calcular_perimetro(self):
        print("Perímetro:", 2 * 3.1415 * self.radio)

circulo1 = Circulo(5)
circulo1.calcular_area()
circulo1.calcular_perimetro()
