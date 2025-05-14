
class Mensaje:
    def __init__(self, contenido):
        self.contenido = contenido

    def mostrar_mensaje(self):
        print(f"Mensaje: {self.contenido}")


class Alerta(Mensaje):
    pass


notificacion = Alerta("¡Cuidado! Batería baja.")
notificacion.mostrar_mensaje()
