#Define una clase 'Mensaje' con un método que imprima un mensaje. Luego crea otra clase 'Alerta' que herede de 
#'Mensaje' sin modificarlo

class Mensaje:
    def Mensajito(self):
        print("Te hemos avisado de un problema")
        
class Alerta(Mensaje):
    def Mensajitos(self):
        return print("Te hemos avisado de un problema")

Hola = Alerta()
Hola.Mensajito()
Hola.Mensajitos()