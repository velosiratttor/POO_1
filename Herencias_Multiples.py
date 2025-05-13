class Persona:
    def __init__(self,nombre,edad,pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        
    def persona_presentar(self):
        print(f"""Hola soy {self.nombre} y tengo la edad de {self.edad}
            y soy del pais de {self.pais}""")
        
class Empleado:
    def __init__(self, cargo,horario,salario):
        self.cargo = cargo
        self.horario = horario
        self.salario = salario
        
    def Empleado_presentar(self):
        print(f"Mi cargo es {self.cargo} y mi horarios es: {self.horario}")
        
class Jefe(Persona,Empleado):
    def __init__(self, nombre, edad, pais,cargo,horario,salario,nombre_empresa,deporte_favorito,comida_favorita):
        Persona.__init__(self,nombre, edad, pais)
        Empleado.__init__(self,cargo,horario,salario)
        self.nombre_empresa = nombre_empresa
        self.deporte_favorito = deporte_favorito
        self.comida_favorita = comida_favorita
        
    def presentar_lider(self):
        print(f"""
            Soy lider de la empresa {self.nombre_empresa}
            Mi comida favorita es: {self.comida_favorita}
            Mi deporte favorito es: {self.deporte_favorito}""")
        
Jefe1 = Jefe("Samuel",20,"Nicaragua","Jefe","8:00 am - 12:00 md",40000,"Codelad","Beisball","pollo")

Jefe1.Empleado_presentar()
Jefe1.persona_presentar()
Jefe1.presentar_lider()
