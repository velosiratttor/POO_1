#                       Sistema de Control de Proyectos
#En una empresa de desarrollo, un ProjectManager debe heredar atributos de una clase Persona (nombre, edad) y de 
# una clase Proyecto (nombre del proyecto, duración). Crea la clase ProjectManager que use herencia múltiple y 
# tenga un método para mostrar toda su información.

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Mi nombre es {self.nombre} y tengo {self.edad} años")
        
class Proyecto:
    def __init__(self,nombre_proyecto,duracion):
        self.nombre_proyecto = nombre_proyecto
        self.duración = duracion
        print(f"El nombre del proyecto es {self.nombre_proyecto} y la duracion es de {self.duración} dias")
        
class ProyectManager(Persona,Proyecto):
    def __init__(self, nombre, edad,nombre_proyecto,duracion,comida_del_equipo):
        Persona.__init__(self,nombre, edad)
        Proyecto.__init__(self,nombre_proyecto,duracion)
        self.comida_del_equipo = comida_del_equipo
        
    def presentar(self):
        print(f"El equipo le damos de comer {self.comida_del_equipo}")
        
Proyectox = ProyectManager("Samuel",20,"Hackaton",2,"Carne asada")
Proyectox.presentar()