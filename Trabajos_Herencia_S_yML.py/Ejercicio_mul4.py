#                               Gestión de Eventos Empresariales
#Crea una clase Persona con atributos nombre y rol, y una clase Evento con atributos tipo_evento y fecha. Luego 
# crea una clase Coordinador que herede de ambas y permita registrar un evento con el coordinador responsable. 
# Crea un método que muestre todos los datos involucrados

class Persona:
    def __init__(self,nombre,rol):
        self.nombre = nombre 
        self.rol = rol 
        print(f"Mi nombre es {self.nombre} y mi rol es {self.rol}")
        
class Evento:
    def __init__(self,tipo_evento,fecha):
        self.tipo_evento = tipo_evento
        self.fecha = fecha
        print(f"El tipo de evento es: {self.tipo_evento} y la fecha de inicio es {self.fecha}")
        
class Coordinador(Persona,Evento):
    def __init__(self, nombre, rol,tipo_evento,fecha,edad):
        Persona.__init__(self,nombre, rol)
        Evento.__init__(self,tipo_evento,fecha)
        self.edad = edad
        
        if edad >= 18 :
            print(f"Puede entrar al evento con {self.edad}")
        else:
            print(f"No puedes entrar al evento por menor de {self.edad}")
            
    def mostrar(self):
        print("Todo listo")
evento = Coordinador("Samuel","Programador","Hackathon","20 de septiembre",16)
evento.mostrar()
