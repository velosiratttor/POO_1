#Haz una clase 'Matematica' con un método para multiplicar dos números. Luego crea una clase 'EjerciciosMatematicos'
#que use ese método

class Matematica:
    def multiplicar(self):
        print ("Multiplicar el numero 2 ")
        
    def multipicar2(self):
        print ("por el 1")
        
class Ejercicio_matematicos(Matematica):
    def Ejer_matematicos(self):
        print ("La multiplicacion de 2 por 1 es : 2 ")
        
metodos = Ejercicio_matematicos()
metodos.multiplicar()
metodos.multipicar2()
metodos.Ejer_matematicos()