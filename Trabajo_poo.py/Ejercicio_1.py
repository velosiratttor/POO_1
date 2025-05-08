#crea una clase llamada 'Persona' con los atributos nombre y edad. Agrega un método que imprima un saludo con el 
#nombre.



class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def presentar(self):
        print(f"Hola {self.nombre} tienes {self.edad} puedes ser mi compañero")

persona_1 = Persona("Samuel","20 años")

persona_1.presentar()
