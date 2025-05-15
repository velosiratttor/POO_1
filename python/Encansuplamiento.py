class persona:
        def __init__(self,nombre,edad,usuario,contraseña):
                   self.nombre=nombre #public
                   self.edad=edad #public
                   self._usuario=usuario #protected
                   self.__contraseña=contraseña #privado

        def get__contraseña(self):
                return self.__contraseña
        
        def set_contraseña(self,new__contraseña):
                self.__contraseña=new__contraseña

persona1=persona('jose',25,'pereira', 1234)

print(persona1.nombre)
print(persona1._usuario)
print(persona1.get__contraseña())
persona1.set_contraseña('123b')
print(persona1.get__contraseña())
                   