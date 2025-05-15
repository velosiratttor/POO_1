#Programar una clase `UsuarioSistema` que use propiedades 
#para validar formatos de correo electrónico y contraseñas.
class UsuarioSistema:
    def __init__(self, correo, contraseña):
        self.correo = correo
        self.contraseña = contraseña

    def correo_valido(self):
        return "@" in self.correo and "." in self.correo

usuario = UsuarioSistema("correo@ejemplo.com", "1234")
print(usuario.correo_valido())  # con paréntesis
