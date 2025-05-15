#Crea una clase llamada Empleado que contenga el 
# nombre del empleado y su sueldo.  El atributo del 
# sueldo debe ser privado. Agrega una propiedad para 
# acceder y  modificar el sueldo,asegurándote 
# de que no pueda establecerse un sueldo negativo. 
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.__sueldo = sueldo

    @property
    def sueldo(self):
        return self.__sueldo

    @sueldo.setter
    def sueldo(self, nuevo_sueldo):
        if nuevo_sueldo >= 0:
            self.__sueldo = nuevo_sueldo
        else:
            print("Error: El sueldo no puede ser negativo.")


empleado = Empleado("Ana", 3000)
print(empleado.sueldo)
empleado.sueldo = 3500
empleado.sueldo = -100  
