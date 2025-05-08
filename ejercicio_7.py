#7. Crea una clase 'Estudiante' que almacene el nombre, edad y promedio. Agrega un método que indique si el estudiante está aprobado (promedio >= 60).

class Estudiante:
    
    def __init__(self,nombre,edad,promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio
        
    def Calificacion(self):
       
       if self.promedio >=60:
        return print(f"El estudiante aprobo?  {self.nombre} si aprobo ya que su promedio es de {self.promedio}")
       else:
        return print(f"{self.nombre} no aprobo su promedio es bajo  y es de {self.promedio}")

estudiante = Estudiante("Gabriel",18,98)
estudiante_2 = Estudiante("Anthony",19,42)

estudiante.Calificacion()
estudiante_2.Calificacion()