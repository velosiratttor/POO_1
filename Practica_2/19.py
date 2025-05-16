#Usar `abc` para una clase abstracta `Servicio` y derivar 
# servicios como `Mantenimiento`, `Consultoría`, etc.
class servicio:
    def ejecutar(self):
        pass

class mantenimiento(servicio):
    def ejecutar(self):
        return "Ejecutando mantenimiento"

class Consultoria(servicio):
    def ejecutar(self):
        return "Realizando consultoría"


s = mantenimiento()
print(s.ejecutar()) 
