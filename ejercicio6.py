#6. Implementa una clase 'Rectángulo' con atributos base y altura, y métodos para calcular el área y el perímetro.
class Rectangulo:
    
    def __init__(self, base , altura):
        self.base = base
        self.altura = altura
        
    def calcular_area_perimetro(self, largo, ancho):
        
        self.area = self.base * self.altura
        self.perimetro = largo * ancho
        print(f'El area del rectangulo: {self.area} y el perimetro es: {self.perimetro}')
        
rectangulo1 = Rectangulo(base=10,altura=20)

rectangulo1.calcular_area_perimetro(40,20)