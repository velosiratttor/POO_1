#Usar `abc` para una clase abstracta `Servicio` y derivar 
# servicios como `Mantenimiento`, `Consultoría`, etc.
class Servicio:
    def ejecutar(self):
        pass

class Mantenimiento(Servicio):
    def ejecutar(self):
        return "Ejecutando mantenimiento"

class Consultoria(Servicio):
    def ejecutar(self):
        return "Realizando consultoría"


s = Mantenimiento()
print(s.ejecutar()) 
