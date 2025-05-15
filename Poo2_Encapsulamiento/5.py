#Implementa una clase GerenteProyecto con nombre 
#y una puntuación de  rendimiento (0 a 100). 
#Usa `@property` para asegurar que la puntuación 
#no pueda  establecerse fuera de ese rango.
class GerenteProyecto:
    def __init__(self, nombre, puntuacion):
        self.nombre = nombre
        self.__puntuacion = 0
        self.puntuacion = puntuacion  # Usa setter

    @property
    def puntuacion(self):
        return self.__puntuacion

    @puntuacion.setter
    def puntuacion(self, nueva_puntuacion):
        if 0 <= nueva_puntuacion <= 100:
            self.__puntuacion = nueva_puntuacion
        else:
            print("Error: La puntuación debe estar entre 0 y 100.")


gerente = GerenteProyecto("Claudia", 85)
print(gerente.puntuacion)
gerente.puntuacion = 110  
