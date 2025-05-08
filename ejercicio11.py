#11. Diseña una clase 'Punto' con coordenadas x e y. Agrega un método para calcular la distancia a otro punto.

class punto:
    
    def __init__(self, x , y):
        self.x = x
        self.y = y
    
    def calcular_distancia(self):
        resultado = self.x*(self.y * 100)
        return f'Y: es una distancia son distancia de {self.y} metros  cuanto es centimetros "x" para llegar a y : {resultado} es la distancia que necesita' 

punto1 = punto(10 , 50)
print(punto1.calcular_distancia())