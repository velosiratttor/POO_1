#Crea una clase 'Producto' con atributos nombre y precio. Agrega un método para aplicar un descuento dado un 
#porcentaje. 

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def Aplicar(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        precio_final = self.precio - descuento
        print(f"Producto: {self.nombre}")
        print(f"Precio original: {self.precio:.2f}")
        print(f"Descuento aplicado: {porcentaje}%")
        print(f"Precio con descuento: {precio_final:.2f}")

producto = Producto("Audífonos", 120.00)
producto.Aplicar(20)
