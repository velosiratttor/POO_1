#En un sistema de inventario, define una clase 
# Producto con los atributos nombre y precio. 
# Luego, crea una clase ProductoImportado que herede 
# de Producto y añada un atributo de impuesto de importación. 
#Implementa un método que calcule el precio final 
# del producto considerando el impuesto.

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class ProductoImportado(Producto):
    def __init__(self, nombre, precio, impuesto):
        super().__init__(nombre, precio)
        self.impuesto = impuesto  # en porcentaje, por ejemplo 15 para 15%

    def precio_final(self):
        total = self.precio + (self.precio * self.impuesto / 100)
        print(f"Producto: {self.nombre}, Precio Final: {total}")

# Ejemplo
p = ProductoImportado("Laptop", 1000, 20)
p.precio_final()
