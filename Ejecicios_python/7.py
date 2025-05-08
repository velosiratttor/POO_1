class Estudiante:
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    def esta_aprobado(self):
        if self.promedio >= 60:
            print("El estudiante está aprobado.")
        else:
            print("El estudiante no está aprobado.")

est = Estudiante("Luis", 18, 100)
est.esta_aprobado()
