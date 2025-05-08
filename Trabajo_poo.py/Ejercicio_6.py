#Implementa una clase 'Rectángulo' con atributos base y altura, y métodos para
#calcular el área y el perímetro

class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
        
    def Areas (self):
        aria = self.base * (self.altura)
        return aria
    
    def Perimetro (self):
        peri = self.altura * (self.base)
        
mi_rectangulo = Rectangulo(2,2)

print("El area por el perimetro es: ",mi_rectangulo.Areas())
