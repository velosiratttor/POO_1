class Laptop():
    marca = "toxhiba"
    pantalla = "14"
    procesador = "i5"
    disco = "250 gb"
    memoria = "8 gb"
    color = "rojo"

laptop_1 = Laptop()
laptop_2 = Laptop()

print(laptop_1.marca,laptop_1.pantalla)
print(laptop_2.color)


class Laptop:
    
    def __init__(self,marca,pantalla,procesador,disco,memoria,color):
        self.marca = marca
        self.pantalla = pantalla
        self.procesador = procesador
        self.disco = disco
        self.memoria = memoria
        self.color = color 
        
    def presentar(self):
        print(f"la marca es {self.marca} y es una gran marca")
        
    def descuento(self):
        print(f"Esta marca tiene un descuento del 15% por ser procesador {self.procesador}")
laptop_1 = Laptop("hp","14","i5","250gb","8gb", "rojo")

print (laptop_1.marca,laptop_1.pantalla)

laptop_1.presentar()
laptop_1.descuento()
