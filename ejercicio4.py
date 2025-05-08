#4. Crea una clase 'Auto' con atributos marca, modelo y año. Agrega un método que devuelva la descripción completa del auto.

class auto :
    
    def __init__(self , marca , modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def mostrar(self):
        return f'Auto: {self.marca} , {self.modelo} , {self.año}'
    
auto1 = auto('Lamborghini' , 'Veneno', '2018')
print(auto1.mostrar())