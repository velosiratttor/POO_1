#Diseña una clase 'Reloj' con atributos hora, minuto y segundo. Agrega un método para mostrar la hora en formato 
# HH:MM:SS. 

class Reloj:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def mostrar_hora(self):
        
        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"


reloj = Reloj(9, 5, 3)
print(reloj.mostrar_hora())  
