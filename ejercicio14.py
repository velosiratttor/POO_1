#14. Diseña una clase 'Reloj' con atributos hora, minuto y segundo. Agrega un método para mostrar la hora en formato HH:MM:SS.

class reloj:
    
    def __init__(self, segundo,minutos,horas):
        self.segundo = segundo
        self.minutos = minutos
        self.horas = horas
    
    def mostrar_formato(self):
        
        if self.horas <= 12 and self.minutos <= 60 and self.segundo <= 60:
            return f'{self.horas}:{self.minutos}:{self.segundo}'
        else:
            print('Error en el formato')
reloj1 = reloj(horas=12,minutos=45,segundo=12)
print(reloj1.mostrar_formato())