#13. Implementa una clase 'Agenda' que permite agregar, buscar y mostrar contactos.

class Agenda:
    def __init__(self):
        self.contactos = {} 
        
    def agregar_contacto(self, nombre, numero):
        
        if nombre in self.contactos:
            print(f"El contacto '{nombre}' ya existe en la agenda.")
        else:
            self.contactos[nombre] = numero
            print(f"Contacto '{nombre}' agregado a la agenda.")

    def buscar_contacto(self, nombre):
       
        if nombre in self.contactos:
            return self.contactos[nombre]
        else:
            return f"No se encontró ningún contacto con el nombre '{nombre}'."

    def mostrar_contactos(self):
        
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            print("\n--- Lista de Contactos ---")
            for nombre, numero in self.contactos.items():
                print(f"Nombre: {nombre}, Número: {numero}")
            print("---------------------------\n")

mi_agenda = Agenda()

mi_agenda.agregar_contacto("Juan Pérez", "1234-5678")
mi_agenda.agregar_contacto("Martin Gómez", "9876-5432")
mi_agenda.agregar_contacto("Juan Pérez", "1111-2222") 

mi_agenda.mostrar_contactos()

print(f"Número de Juan Pérez: {mi_agenda.buscar_contacto('Juan Pérez')}")
print(f"Número de Carlos Ruiz: {mi_agenda.buscar_contacto('Carlos Ruiz')}")

mi_agenda.agregar_contacto("Pedro López", "5555-1212")
mi_agenda.mostrar_contactos()