#Crea una clase 'Accion' con un método que diga 'Ejecutando acción'. Luego haz una clase 'AccionRapida'
#que use ese método heredado.

class Accion:
    def Ejecutando_acción(self):
        print("Ejecutando acción")
        
class Accion_rapido(Accion):
    def Activo(self):
        print("Accion rapida")
        
accion1  = Accion_rapido()
accion1.Activo()
accion1.Ejecutando_acción()