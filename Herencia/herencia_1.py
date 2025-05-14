class Animal:

           def correr(self):
                   print("Puedo correr")
           
           def cazar(self):
                   print("Puedo cazar")

#Herencia simple / esta clase es clase hija
class Perro(Animal):
        def Ladrar(self):
                print('Puedo ladrar')
        def Cuidar(self):
                print('Puedo cuidar tu casa')

Perro1 = Perro()
Perro1.correr()