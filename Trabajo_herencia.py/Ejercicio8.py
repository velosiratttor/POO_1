#Haz una clase 'Producto' con 'nombre' y 'precio', y un método para mostrar la información. Luego una clase 'Libro' 
#que herede esos datos.

class Producto:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio
        
    def Metodo(self):
        print(f"El libro se llama {self.nombre} y el precio es de {self.precio}")
        
class libro(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        
producto1 = libro("Cristiano Ronaldo","200 euro")
producto1.Metodo()