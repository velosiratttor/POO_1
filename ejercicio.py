class Persona :
    
    def __init__(self , nombre , edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludo(self):
        print(f'Hola Sen@r {self.nombre}')

Persona1 = Persona('MarcElson', 20)
Persona1.saludo()
        
