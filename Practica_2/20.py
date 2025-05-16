#Crear una clase abstracta `Notificador` y heredar 
#`Correo`, `SMS` y `NotificaciónPush` para diferentes medios.
class notificador:
    def enviar(self, mensaje):
        pass

class correo(notificador):
    def enviar(self, mensaje):
        print("Correo enviado:", mensaje)

class SMS(notificador):
    def enviar(self, mensaje):
        print("SMS enviado:", mensaje)

class notificacionpush(notificador):
    def enviar(self, mensaje):
        print("Push enviado:", mensaje)

n = SMS()
n.enviar("Tu código es 1234") 
