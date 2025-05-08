#11. Diseña una clase 'Punto' con coordenadas x e y. Agrega un método para calcular la distancia a otro punto.
        
import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)
        return distancia

punto1 = Punto(1, 2)
punto2 = Punto(4, 6)

distancia = punto1.calcular_distancia(punto2)
print(f"La distancia entre el punto ({punto1.x}, {punto1.y}) y ({punto2.x}, {punto2.y}) es: {distancia:.2f}")

punto3 = Punto(-1, 0)
distancia2 = punto1.calcular_distancia(punto3)
print(f"La distancia entre el punto ({punto1.x}, {punto1.y}) y ({punto3.x}, {punto3.y}) es: {distancia2:.2f}")