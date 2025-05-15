#                                 Producto en Inventario 
#iseña una clase Producto con nombre, código y stock. El stock debe ser privado y
#solo puede modificarse a través de métodos que verifiquen que no se coloque un
#número negativo. 


class Producto:
    def __init__(self,nombre,codigo,stock):
        self.nombre = nombre #public
        self.codigo = codigo # public
        self.__stock = stock #privado
        
    def get_stock(self):
        return self.__stock
    
    def set_stock(self,new__stock):
        self.__stock = new__stock
        if self.__stock < 0 :
            print("NO ESCRIBIR NUMEROS NEGATIVOS")
        else:
            print(f"El stock esta en",self.__stock)
producto1 = Producto("Clavos","55B",100)

print("El produto es : ",producto1.nombre)
print("El codigo del producto es :",producto1.codigo)
producto1.set_stock(100)

