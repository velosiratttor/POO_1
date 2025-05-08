class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        precio_final = self.precio - descuento
        print(f"Precio con {porcentaje}% de descuento: {precio_final}")

producto = Producto("Laptop", 1000)
producto.aplicar_descuento(10)


                   