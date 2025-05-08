#9. Crea una clase 'Producto' con atributos nombre y precio. Agrega un método para aplicar un descuento dado un porcentaje.

class Producto:
    
    def __init__(self, nombre , precio):
        self.nombre = nombre
        self.precio = precio
    
    def calculo_descuento (self, descuento):
        self.descuento = self.precio - ((self.precio * descuento) / 100)
        print(f'Producto: {self.nombre} , precio: {self.precio}, precio con descuento {self.descuento}')

coca = Producto('coca-cola', 20)

coca.calculo_descuento(5)