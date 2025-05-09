#Agregar 3 metodos mas animal y crear 3 nuevas clases hijas que hereden de la clase padre animal con metodos propios de ellas.

class Animal:
    
    def Dormir(self):
        print("duermo todas las noches")
        
    def Comer(self):
        print("puedo comer demasiado")
        
class Gato(Animal):
    def Maullar(self):
        print("maullo todas las noches")
    def Saltar(self):
        print("puedo saltar alto")
        
class Caballo(Animal):
    def Relinchar(self):
        print("puedo Relinchar todo el dia")
    
    def Correr(self):
        print("puedo correr muchos KM")
        
class Lora(Animal):
    def Hablar(self):
        print("puedo hablar repitiendo a los humanos")
        
    def Volar(self):
        print("puedo volar muy alto")
        
gato1=Gato()
gato1.Saltar()

caballo2=Caballo()
caballo2.Correr()

Lora3=Lora()
Lora3.Hablar()