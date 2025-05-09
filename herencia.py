class Animal:
    
    def correr(self):
        print("puedo correr")
        
    def cazar(self):
        print("puedo cazar")
        
#herencia simple / esta clase es clase una hija
class Perro(Animal):
    def ladrar(self):
        print("puedo ladrar")
    def cuidar(self):
        print("puedo cuidar tu casa")
        
perro1=Perro()
perro1.correr()