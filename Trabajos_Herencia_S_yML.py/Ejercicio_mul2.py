#                           Asistente Administrativo con Múltiples Roles
#Crea una clase Administrativo con un método gestionar_documentos() y una clase Tecnico con un método 
# resolver_problemas(). Luego crea una clase Asistente que herede de ambas y tenga la capacidad de ejecutar ambos 
# métodos. Simula el trabajo diario de un asistente multitareas.

class Administracion:
    
    def gestionar_documentos(self):
        print("Necesito que me gestiones unos documentos de el tecnico")
        
class Tecnico:
    
    def resolver_problemas(self):
        print("El problema es que no esta haciendolo como te estoy correspondiendo")
        
class Asistente(Administracion, Tecnico):
        pass

Asistente1 = Asistente()
Asistente1.gestionar_documentos()
Asistente1.resolver_problemas()
