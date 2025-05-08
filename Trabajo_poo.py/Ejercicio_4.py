#Crea una clase 'Auto' con atributos marca, modelo y año. Agrega un método que devuelva la descripción completa del 
#auto.

class Auto:
    def __init__(self,Marca,modelo,año):
        self.marca = Marca
        self.modelo = modelo
        self.año = año
        
    def Marca_1(self):
        print(f"La marca del auto es {self.marca}, el modelo es {self.modelo} y del año")
        
mi_auto = Auto("Supra","GTR35","2015")

mi_auto.Marca_1()