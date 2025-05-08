import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia_a(self, otro):
        distancia = math.sqrt((self.x - otro.x)**2 + (self.y - otro.y)**2)
        print("Distancia:", distancia)

p1 = Punto(0, 0)
p2 = Punto(3, 4)
p1.distancia_a(p2)
