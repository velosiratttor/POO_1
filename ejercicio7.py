#7. Crea una clase 'Estudiante' que almacene el nombre, edad y promedio. Agrega un método que indique si el estudiante está aprobado (promedio >= 60).

class Estudiante:
    def __init__(self, nombre ,edad,nota1,nota2,nota3,nota4):
        self.nombre = nombre
        self.edad = edad
        self.nota = [nota1,nota2,nota3,nota4]
    
    def calculo_promedio(self):
        self.promedio = (sum(self.nota))/len(self.nota)
        print(f'Promedio de este estudiante: {self.nombre} edad = {self.edad} es de : {self.promedio}')

estudiante_random = Estudiante ('Mael', 15,nota1= 60,nota2=34,nota3=90,nota4=80)
estudiante_random.calculo_promedio()