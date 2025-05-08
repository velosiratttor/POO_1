#8. Diseña una clase 'Libro' con atributos título, autor y año. Agrega un método para mostrar la información del libro.

class Libro:
    
    def __init__(self,titulo,autor,año):
        self.titulo = titulo 
        self.autor = autor
        self.año = año
        
    def Informacion(self):
        print(f"Este libro se titula {self.titulo} y su autor es {self.autor} y fue lanzado el año {self.año}")
        
libro = Libro("Cien años de soledad","Gabriel Garcia Marquez","1967")

libro.Informacion()