class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")


class profesor(persona):
    pass


profe = profesor("Laura", 42)
profe.presentarse()
