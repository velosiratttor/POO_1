class Persona:
    def __init__(self,nombre,edad,usuario,contraseña):
        self.nombre = nombre #public
        self.edad = edad #public
        self._usuario = usuario #protected
        self.__contraseña = contraseña #privado
        
    def get_contraseña(self):
        return self.__contraseña
        
    def set_contraseña(self,new_contraseña):
        self.__contraseña = new_contraseña
        
persona1 = Persona("Samuel",20,"Gordo Yt",2550)

print(persona1.nombre)
print(persona1._usuario)
print(persona1.get_contraseña())
persona1.set_contraseña("1525l")
print(persona1.get_contraseña())