#Diseña una clase 'Punto' con coordenadas x e y. Agrega un método para calcular la distancia a otro punto

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia_a(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        return ((dx ** 2) + (dy ** 2)) ** 0.5

p1 = Punto(3, 4)
p2 = Punto(0, 0)
print("Distancia:", p1.distancia_a(p2))  
