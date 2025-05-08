class Reloj:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def mostrar_hora(self):
        print(f"{self.hora:02}:{self.minuto:02}:{self.segundo:02}")

reloj = Reloj(9, 5, 3)
reloj.mostrar_hora()
