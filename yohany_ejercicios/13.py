class Agenda:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono
        print("Contacto agregado.")

    def buscar_contacto(self, nombre):
        if nombre in self.contactos:
            print(f"{nombre}: {self.contactos[nombre]}")
        else:
            print("Contacto no encontrado")

    def mostrar_contactos(self):
        for nombre, telefono in self.contactos.items():
            print(f"{nombre}: {telefono}")

agenda = Agenda()
agenda.agregar_contacto("Moises", "82364070")
agenda.buscar_contacto("Moises")
agenda.mostrar_contactos()
