#Una empresa de educación online necesita manejar cursos
#  presenciales y virtuales. Crea una clase Curso con 
# atributos título y duración. Después, crea una clase 
# CursoVirtual que herede de Curso y agregue el atributo 
# plataforma. Implementa un método que muestre toda 
# la información del curso virtual.
class Curso:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion

class CursoVirtual(Curso):
    def __init__(self, titulo, duracion, plataforma):
        super().__init__(titulo, duracion)
        self.plataforma = plataforma

    def mostrar_info(self):
        print(f"Título: {self.titulo}, Duración: {self.duracion} horas, Plataforma: {self.plataforma}")


titulo = input("Título del curso: ")
duracion = int(input("Duración (horas): "))
plataforma = input("Plataforma del curso: ")

curso = CursoVirtual(titulo, duracion, plataforma)
curso.mostrar_info()

