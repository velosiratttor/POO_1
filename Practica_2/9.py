#Desarrollar una clase `TurnoTrabajo` para calcular horas
#  trabajadas y horas extra en distintos roles.
class turnotrabajo:
    def __init__(self, horas_trabajadas):
        self.horas_trabajadas = horas_trabajadas

    def horas_extra(self):
        return max(0, self.horas_trabajadas - 8)


turno = turnotrabajo(10)
print(turno.horas_extra())  
