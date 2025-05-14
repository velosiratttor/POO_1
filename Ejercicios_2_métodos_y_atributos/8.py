class producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        print(f"Producto: {self.nombre}, Precio: ${self.precio}")


class libro(producto):
    pass

libro = libro("Cien años de soledad", 250)
libro.mostrar_info()
