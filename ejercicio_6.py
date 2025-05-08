#6. Implementa una clase 'Rectángulo' con atributos base y altura, y métodos para calcular el área y el perímetro.

class Rectangulo:
    
    def __init__(self,base,altura,):
        self.base = base
        self.altura = altura
        
    def Metodo(self):
        print(f"la formula del calculo es {self.base} x {self.altura}")
        
    def Metodo_2(self):
        print(f"La formula para el perimetro es= 2x {self.base} + {self.altura}")

rectangulo = Rectangulo("28","7")

rectangulo.Metodo()
rectangulo.Metodo_2()
