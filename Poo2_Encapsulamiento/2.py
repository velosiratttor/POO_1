#Diseña una clase Producto con nombre, código y stock. 
#El stock debe ser privado y  solo puede modificarse 
# a través de métodos que verifiquen que no se 
# coloque un  número negativo. 
class Producto:
    def __init__(self, nombre, codigo, stock):
        self.nombre = nombre
        self.codigo = codigo
        self.__stock = stock

    @property
    def stock(self):
        return self.__stock

    def actualizar_stock(self, nuevo_stock):
        if nuevo_stock >= 0:
            self.__stock = nuevo_stock
        else:
            print("Error: El stock no puede ser negativo.")


producto = Producto("Laptop", "A123", 10)
print(producto.stock)
producto.actualizar_stock(15)
producto.actualizar_stock(-5)  
