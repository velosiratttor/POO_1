#                                        Empleado y Sueldo
#Crea una clase llamada Empleado que contenga el nombre del empleado y su sueldo.
#El atributo del sueldo debe ser privado. Agrega una propiedad para acceder y
#modificar el sueldo, asegurándote de que no pueda establecerse un sueldo negativo.

class Empleado:
    def __init__(self,nombre_empleado,sueldo):
        self.nombre_empleado = nombre_empleado # public
        self.__sueldo = sueldo # privado
        
    def get_sueldo(self):
        return self.__sueldo
    
    def set_sueldo(self,new__sueldo):
        self.new__sueldo = new__sueldo
        if self.new__sueldo < 0 :
            print("El salario no puede ser negativo")
        
empleado1 = Empleado("Samuel",5000)

print(empleado1.nombre_empleado)
empleado1.set_sueldo(5000)
print(empleado1.new__sueldo)

