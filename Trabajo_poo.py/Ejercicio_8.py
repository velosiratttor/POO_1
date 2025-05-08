#Diseña una clase 'Libro' con atributos título, autor y año. Agrega un método para mostrar la información del libro.

class Libro:
    def __init__(self,Titulo,autor,año):
        self.Titulo = Titulo
        self.autor = autor
        self.año = año
        
    def mostrar(self):
        print("El Titulo del libro es: ", self.Titulo)
        print("El autor del libro es: ", self.autor)
        print("El año que fue publicado el libro fue: ", self.año)
        
Titulo = input("Escribe el Titulo del libro: ")
autor = input("Escribel el autor del libro: ")
año = float(input("Escribe el año que se publico el libro: "))

libros = Libro(Titulo, autor, año)
libros.mostrar()