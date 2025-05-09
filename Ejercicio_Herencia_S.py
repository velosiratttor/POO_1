class Animal:
    def  dormir(self):
        print("ESTOY DURMIENDO")
        
    def leer(self):
        print("ESTOY LEYENDO")
        
class Cocodrilo(Animal):
    def comer(self):
        print("COMO,COMO,COMO")
        
    def matar(self):
        print("MATAR,MATAR")
        
class Elefante(Animal):
    def tomar_agua(self):
        print("gu, gu, gu")
        
    def trompa(self):
        print("Fuuu, Fuuuu")
        
class Gato(Animal):
    def auyar(self):
        print("Miau, Miau")
        
    def dormirs(self):
        print("ESTOY MIMIENDO")
        
Good = Gato()
Good.dormir()