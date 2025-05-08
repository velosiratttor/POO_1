class circulo :
    
    def __init__(self , area , radio , perimetro , diametro):
        self.area = area
        self.radio = radio
        self.perimetro = perimetro
        self.diametro = diametro
        self.pi = 3.1415
    
    def calcular_circulo(self):
        self.area = self.pi * (self.radio**2)
        self.perimetro = self.pi *(self.diametro)
        print(f'El area del circulo: {self.area} , El perimetro del circulo: {self.perimetro}')

circulo1 = circulo(10,5,10,50)
circulo1.calcular_circulo()