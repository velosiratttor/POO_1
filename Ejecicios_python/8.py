class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def mostrar_informacion(self):
        print(f"'{self.titulo}' por {self.autor}, publicado en {self.año}")

libro1 = Libro("1984", "George Orwell", 1949)
libro1.mostrar_informacion()
