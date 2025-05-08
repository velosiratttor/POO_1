Marca_laptop1= 'toshiba'
Pantalla_laptop1= '14"'
Procesador_laptop1= 'i5'
Disco_laptop1= '250 gb'
Memoria_laptop1= '8 gb'
Marca_laptop2= 'hp'
Pantalla_laptop2= '14"'
Procesador_laptop2= 'i7'
Disco_laptop2= '250 gb'
Memoria_laptop2= '8 gb'

print(Marca_laptop1,Pantalla_laptop1)

class Laptop():
           Marca= 'toshiba'
           Pantalla= '14"'
           Procesador= 'i5'
           Disco= '250 gb'
           Memoria= '8 gb'
           Color='rojo'

laptop1=Laptop()
laptop2=Laptop()

class Laptop:
        
           def __init__(self,Marca,Pantalla,Procesador,Disco,Memoria,Color):
                self.Marca=Marca
                self.Pantalla=Pantalla
                self.Procesador=Procesador
                self.Disco=Disco
                self.Memoria=Memoria
                self.Color=Color

           def presentar(self):
                   print(f'la marca {self.Marca} y es una gran marca')
           
           def descuento(self):
                   print(f'esta marca tiene un descuento del 15% por ser procesador {self.Procesador}')

laptop1=Laptop('hp','14"','i5', '250 gb', '8gb','rojo')
laptop1=Laptop('toshiba','15"','i7','500gb','16g','azul')

print(laptop1.Marca,laptop1.Pantalla)
laptop1.presentar()
laptop1.descuento()