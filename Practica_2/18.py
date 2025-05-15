#Simular un sistema `ReservaSala` con clases que
# validen horarios disponibles y ocupados.
class ReservaSala:
    def __init__(self):
        self.horas_reservadas = []

    def reservar(self, hora):
        if hora in self.horas_reservadas:
            return "Hora ocupada"
        self.horas_reservadas.append(hora)
        return "Reserva confirmada"


ReservaSala = ReservaSala()
print(res.reservar("10:00"))  
print(res.reservar("10:00"))  
