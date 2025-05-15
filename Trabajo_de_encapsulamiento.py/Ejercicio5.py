#                                       Gerente de Proyecto 
#Implementa una clase GerenteProyecto con nombre y una puntuación de
#rendimiento (0 a 100). Usa `@property` para asegurar que la puntuación no pueda
#establecerse fuera de ese rango. 


class GerenteProyecto:
    def __init__(self, nombre, puntuacion=0):
        self.nombre = nombre
        self._puntuacion = 0
        self.puntuacion = puntuacion  

    @property
    def puntuacion(self):
        return self._puntuacion

    @puntuacion.setter
    def puntuacion(self, valor):
        if 0 <= valor <= 100:
            self._puntuacion = valor
        else:
            print("Error: la puntuación debe estar entre 0 y 100.")


g = GerenteProyecto("Carlos", 70)
print(g.nombre)       
print(g.puntuacion)   

g.puntuacion = 80    
print(g.puntuacion)   
