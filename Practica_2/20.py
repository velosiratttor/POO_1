#Crear una clase abstracta `Notificador` y heredar 
#`Correo`, `SMS` y `NotificaciónPush` para diferentes medios.
class Notificador:
    def enviar(self, mensaje):
        pass

class Correo(Notificador):
    def enviar(self, mensaje):
        print("Correo enviado:", mensaje)

class SMS(Notificador):
    def enviar(self, mensaje):
        print("SMS enviado:", mensaje)

class NotificacionPush(Notificador):
    def enviar(self, mensaje):
        print("Push enviado:", mensaje)

n = SMS()
n.enviar("Tu código es 1234") 
