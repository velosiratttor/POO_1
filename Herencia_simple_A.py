class Deporte:
    def __init__(self,nombre_deporte):
        self.nombre_deporte = nombre_deporte
        
    def Dificultad(self):
        if self.nombre_deporte == "baseball":
            print("Dificuldad moderada")
        elif self.nombre_deporte == "basketball":
            print("dificuldad dificil")
            
class Deportista(Deporte):
    def __init__(self,nombre_deporte,nombre_persona,edad):
        super().__init__(nombre_deporte)
        self.nombre_persona = nombre_persona
        self.edad = edad
        
persona1 = Deportista("baseball","jose",25)
persona2 = Deportista("basketball","Cristiano",19)
persona1.Dificultad()
persona2.Dificultad()