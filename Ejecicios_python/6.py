class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        print("Área:", self.base * self.altura)

    def calcular_perimetro(self):
        print("Perímetro:", 2 * (self.base + self.altura))

rect = Rectangulo(4, 5)
rect.calcular_area()
rect.calcular_perimetro()



