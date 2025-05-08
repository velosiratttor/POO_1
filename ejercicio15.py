#15. Crea una clase 'Temperatura' que convierta grados Celsius a Fahrenheit y viceversa.

class Temperatura:
    
    def __init__(self,grados, tipo):
        self.grados = grados
        self.tipo = str(tipo)
    
    def convertir_fahrenheit(self):
        
        if 'Celsius' in self.tipo:
            Fahrenheit = (self.grados * (9/5)) + 32
            print(f'Esta es la cantidad {self.grados} en celsius a Fahrenheit: F°:{Fahrenheit}')
            
        elif 'Fahrenheit' in self.tipo:
            print(f'No se realizo conversion por su solicitud es : C°:{self.grados}')
        else:
            print('Error de conversion')
    
    def convertir_celsius(self):
        
        if 'Fahrenheit' in self.tipo:
            celsius = (self.grados - 32)* 5/9
            print(f'Esta es la cantidad {self.grados} en Fahrenheit a celsius: C°:{celsius}')
        
        elif 'Celsius' in self.tipo:
            print(f'No se realizo conversion por su solicitud es : F°:{self.grados}')
        else:
            print('Error de conversion')
        

Temperatura1 = Temperatura(57, 'Fahrenheit')
Temperatura2 = Temperatura(57, 'Celsius')

Temperatura1.convertir_celsius()
Temperatura2.convertir_fahrenheit()