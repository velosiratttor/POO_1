class accion:
    def __init__(self, nombre_accion):
        self.nombre_accion = nombre_accion

    def ejecutar(self):
        print(f"Ejecutando acción: {self.nombre_accion}")


class accionrapida(accion):
    pass


accion = accionrapida("Reinicio del sistema")
accion.ejecutar()
