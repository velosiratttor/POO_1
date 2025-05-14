#Herencia simple con atributos
class Deporte: 
           def __init__(self, Nombre_deporte):
                   self.Nombre_deporte = Nombre_deporte

           def Dificultad(self):
                   if self.Nombre_deporte == 'Baseball':
                           print(f'Dificultad moderada')
                   elif self.Nombre_deporte == 'Basketball':
                           print(f'Dificultada dificil')
                      
class Deportista(Deporte):
        def __init__(self, Nombre_deporte,  Nombre_persona, Edad):
                super().__init__(Nombre_deporte)
                self.Nombre_persona = Nombre_persona
                self.Edad = Edad

Persona_1 = Deportista('Baseball', 'jose', 25)
Persona_2 = Deportista('Basketball', 'juan', 25)
Persona_1.Dificultad()
Persona_2.Dificultad()
