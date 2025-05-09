#Crea una clase 'Saludo' con un método que diga 'Hola'. Luego crea una clase 'SaludoFormal' que herede ese método.

class Saludo:
    def Hola(self):
        print("Hola")
        
class Saludo_Formal(Saludo):
    def Formal(self):
        print("Hola como esta?")
        
Holaa = Saludo_Formal()
Holaa.Hola()

Holaaa = Saludo_Formal()
Holaaa.Formal()