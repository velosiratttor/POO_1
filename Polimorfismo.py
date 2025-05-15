class Animal:
    def sonido(self):
        print("Hago ruido")
        
class Perro:
    def sonido(self):
        print("Ladro")
        
class Ave:
    def sonido(self):
        print("Canto")
        
#######################################################################

class Ave_2:
    def Volar(self):
        print("Vuelo con un ave")
        
class Avion:
    def Volar(self):
        print("Puedo volar porque soy una maquina")
        
class SuperHeroe:
    def Volar(self):
        print("Puedo volar porque soy un super heroe")
        
        
animal1 = Animal()
chocoyo = Ave()
pitbull = Perro()

colibri = Ave_2()
avioneta = Avion()
superman = SuperHeroe()

colibri.Volar()
avioneta.Volar()
superman.Volar()

animal1.sonido()
chocoyo.sonido()
pitbull.sonido()