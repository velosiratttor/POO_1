#2. Diseña una clase 'Círculo' que tenga un atributo radio y métodos para calcular el área y el perímetro.


class Circulo:
    
    def __init__(self,radio,area,perimetro):
        self.radio = radio
        self.area = area
        self.perimetro = perimetro
        
    def metodo_del_calculo(self):
        print(f"El area se calcula mediante la formula de: pi= 3.1416 x {self.radio} y el perimetro por P=Pi x D P= 3.1416 x {self.area} ")
        
circulo_1 = Circulo("5","78.54","31.42")
        
print(circulo_1.radio,circulo_1.area,circulo_1.perimetro)

circulo_1.metodo_del_calculo()