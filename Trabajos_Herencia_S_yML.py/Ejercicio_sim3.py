# Inventario de Productos Nacionales e Importados

# En un sistema de inventario, define una clase Producto con los atributos nombre y precio. Luego, crea una clase 
# ProductoImportado que herede de Producto y añada un atributo de impuesto de importación. Implementa un método que 
# calcule el precio final del producto considerando el impuesto.

class Producto:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio
        
class Producto_importado(Producto):
    def __init__(self, nombre, precio,impuesto):
        super().__init__(nombre, precio)
        self.impuesto = impuesto
        
    def impuestoss(self):
        porcentajee = self.precio * self.impuesto
        precio_final = self.precio + porcentajee
        print(f"El nombre del producto es: {self.nombre}")
        print(f"El precio sin impuesto es: {self.precio}")
        print(f"EL IMPUESTO FINAL ES: {precio_final:.2f}")
        
importados = Producto_importado("Moto zuzuki",30000,0.06)
importados.impuestoss()
