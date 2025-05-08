#9. Crea una clase 'Producto' con atributos nombre y precio. Agrega un método para aplicar un descuento dado un porcentaje.

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def aplicar_descuento(self, porcentaje_descuento):
        if 0 <= porcentaje_descuento <= 100:
            print("El porcentaje de descuento debe entre 100 y 0")
      
        else:
            print("El porcentaje de descuento debe estar entre 0 y 100.")

producto = Producto("camiseta blanca",250)

producto.aplicar_descuento()