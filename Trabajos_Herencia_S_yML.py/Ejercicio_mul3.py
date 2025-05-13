#                           Sistema de Alerta Meteorológica
#Crea una clase Sensor con el atributo tipo_sensor y una clase Conexion con el atributo protocolo. Luego, crea una 
# clase Alerta que herede de ambas y contenga un método que imprima los datos del sensor y el protocolo usado para 
# transmitir los datos.


class Sensor:
    def __init__(self,tipo_sensor):
        self.tipo_sensor = tipo_sensor
        print(f"El tipo de sensor que necesitamos es: {tipo_sensor}")
        
class Conexion:
    def __init__(self,protocologo):
        self.protocologo = protocologo
        print(f"El protocologo que se necesita es: {self.protocologo}")
        
class Alerta(Sensor, Conexion):
    def __init__(self, tipo_sensor,protocologo):
        Sensor.__init__(self,tipo_sensor)
        Conexion.__init__(self,protocologo)
        
    def mostrar(self):
        print("""Todos los sitemas se encuentran bien""")
        
sistema = Alerta("sistema de calor","Diplomatico")
sistema.mostrar()