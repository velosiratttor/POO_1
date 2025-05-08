#13. Implementa una clase 'Agenda' que permita agregar, buscar y mostrar contactos.

class agenda:
    
    def __init__(self):
        self.notas = []
    
    def agregar (self, notas):
        self.notas.append(notas)
    
    def buscar(self, indice):
        if 0 <= indice < len(self.notas):
            return f'Nota {indice} --> {self.notas[indice]}'
        else:
            return 'Índice de nota no válido.'

    def mostrar(self):
        for i in self.notas:
            print(f'Notas --> {i}')

agenda1 = agenda()
agenda1.agregar('Hola a todos')
agenda1.agregar('como estan')
agenda1.agregar('todoss')

print(agenda1.mostrar())