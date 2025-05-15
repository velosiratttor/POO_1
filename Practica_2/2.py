#Desarrollar una clase `ProductoInventario` para gestionar stock,
#calcular valores totales y aplicar descuentos.
class ProductoInventario:
    def __init__(self, nombre, cantidad, precio_unitario):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def valor_total(self):
        return self.cantidad * self.precio_unitario

    def aplicar_descuento(self, porcentaje):
        return self.precio_unitario * (1 - porcentaje / 100)


p = ProductoInventario("Laptop", 10, 800)
print(p.valor_total())  # 8000
print(p.aplicar_descuento(15))  
