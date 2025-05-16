#Implementar una clase `AgendaReuniones` que organice y filtre 
#reuniones por fecha o prioridad.
class reunion:
    def __init__(self, fecha, prioridad):
        self.fecha = fecha
        self.prioridad = prioridad

class agendareuniones:
    def __init__(self):
        self.reuniones = []

    def agregar_reunion(self, reunion):
        self.reuniones.append(reunion)

    def filtrar_por_prioridad(self, nivel):
        return [r.fecha for r in self.reuniones if r.prioridad == nivel]


agenda = agendareuniones()
agenda.agregar_reunion(reunion("2025-05-15", "Alta"))
agenda.agregar_reunion(reunion("2025-05-16", "Baja"))
print(agenda.filtrar_por_prioridad("Alta"))  