class Deporte:
    def __init__(self,nombre_deporte,horario,fecha_inicio):
        self.nombre_deporte = nombre_deporte
        self.horario = horario
        self.fecha_inicio = fecha_inicio
        
    def dificultad(self):
        if self.nombre_deporte=="baseball":
            print(f"dificultad moderada")
        elif self.nombre_deporte=="basketball":
            print("dificultad dificil")
            
class Deportistas(Deporte):
    def __init__(self,nombre_deporte,horario,fecha_inicio,nombre_persona,edad):
        super().__init__(nombre_deporte,horario,fecha_inicio)
        self.nombre_persona=nombre_persona
        self.edad=edad
        
persona_1=Deportistas("baseball","Gabriel",18)
persona_2=Deportistas("basketball","Anthony",20)
persona_1.dificultad
persona_2.dificultad