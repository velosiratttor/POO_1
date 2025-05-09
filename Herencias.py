class Animal:
    def correr(self):
        print("Puedo correr")
        
    def cazar(self):
        print("Puedo cazar")
        
#Herencias siemples / esta clase es una hija 

class Perro(Animal):
    def ladrar(self):
        print("Puedo ladrar")
        
    def cuidar(self):
        print("puedo cuidar")
        
#perro1 = Perro()
#perro1.correr()


#Herencia simples / clases padres 

class padre(Perro, Animal):
    def raton(self):
        print("Yo soy raton")
        
    def cocodrilo(self):
        print("Yo soy un cocodrilo")
        
coco = padre()
coco.cocodrilo()
coco.cazar()