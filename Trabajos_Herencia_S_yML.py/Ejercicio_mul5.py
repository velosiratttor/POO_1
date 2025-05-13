#                                Control de Calidad en Producción
#Crea una clase Producto con atributos nombre y lote. Crea una clase Evaluacion con atributos resultado y 
# observaciones. Luego, diseña una clase InformeCalidad que herede de ambas y contenga un método que resuma la 
# inspección del producto con base en todos los atributos.

class Producto:
    def __init__(self,nombre,lote):
        self.nombre = nombre
        self.lote = lote
        
class Evaluacion:
    def __init__(self,resultado,observaciones):
        self.resultado = resultado
        self.observaciones = observaciones
        
class Informe_Calidad(Producto,Evaluacion):
    def __init__(self, nombre, lote,resultado,observaciones):
        Producto.__init__(self,nombre, lote)
        Evaluacion.__init__(self,resultado,observaciones)
        
    def mostrar(self):
        print(f"""EL nombre del producto es: {self.nombre}
            El lote es: {self.lote}
            El resultado es {self.resultado}
            Las observaciones son {self.observaciones}""")
        
control = Informe_Calidad("Caja de pez","400 unidades","Es perfecto","Positivas a lo que pedimos")
control.mostrar()