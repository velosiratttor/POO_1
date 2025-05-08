#1. Crea una clase llamada 'Persona' con los atributos nombre y edad. Agrega un método que imprima un saludo con el nombre.



class persona:
   
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludo(self):
            print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años de edad")
            
persona_1 = persona("Gabriel","18")

print(persona_1.nombre,persona_1.edad)

persona_1.saludo()
            