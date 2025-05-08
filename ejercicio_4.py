#4.Crea una clase 'Auto' con atributos marca, modelo y año. Agrega un método que devuelva la descripción completa del auto.


class Auto:
    
    def __init__(self,marca,modelo,año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
    def descripcion(self):
        print(f"Auto de la marca {self.marca} modelo {self.modelo} del año {self.año}")
        
auto = Auto("Toyota","Yaris","2020")

auto.descripcion()