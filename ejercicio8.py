#8. Diseña una clase 'Libro' con atributos título, autor y año. Agrega un método para mostrar la información del libro.

class Libro :
    
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
    
    def mostrar(self):
        print(f'Libro: Titulo: {self.titulo} , Autor: {self.autor} , Año: {self.año}')

libro1 = Libro('Monarca','Pablo Herrero', 1865)
libro1.mostrar()