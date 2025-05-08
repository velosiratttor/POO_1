"""
3. Implementa una clase 'Calculadora' con métodos para sumar, restar, multiplicar y
dividir dos números.
"""
"""class Calculadora:
    def __init__(self,n1, n2,suma, resta, multi, divi):
        self.n1 = n1
        self.n2 = n2
        self.suma = suma
        self.resta = resta
        self.multi = multi
        self.divi = divi
        
    def ingre1(self):
        self.n1 = n1
        
    def ingre2(self):
        self.n2 = float(input())
        
    def sumar(self):
        self.suma = (self.n1) + (self.n2)
        
    def restar(self):
        self.resta = self.n1 - self.n2
        
    def multip(self):
        self.multi = self.n1 * self.n2
    
    def divid(self):
        self.divi = self.n1 / self.n2
        
print(f"Ingrese el primer número: ")
Calculadora.ingre1 = float(input())
print(f"Ingrese el segundo número: ")
Calculadora.ingre2 = float(input())
print(f"La SUMA de los dos números es: ")
Calculadora.sumar()
print(f"La RESTA de los números es: ")
Calculadora.restar()
print(f"La MULTIPLICACIÓN de los números es: ")
Calculadora.multip()
print(f"La DIVISIÓN de los dos número es: ")
Calculadora.divid()
"""

#Versión coorregida de la class Calculadora
import os
os.system("cls")

class Calculadora:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0

    def ingre1(self):
        self.n1 = float(input("Ingrese el primer número: "))

    def ingre2(self):
        self.n2 = float(input("Ingrese el segundo número: "))

    def sumar(self):
        return self.n1 + self.n2

    def restar(self):
        return self.n1 - self.n2

    def multip(self):
        return self.n1 * self.n2

    def divid(self):
        if self.n2 != 0:
            return self.n1 / self.n2
        else:
            return "Error: División por cero"

# Crear una instancia de la clase
calc = Calculadora()

# Usar los métodos
print()
calc.ingre1()
calc.ingre2()
print()
print()

print(f"La SUMA de los números {calc.n1} y {calc.n2} es: {round(calc.sumar(),2)}")
print()
print(f"La RESTA de los números {calc.n1} y {calc.n2} es: {round(calc.restar(),2)}")
print()
print(f"La MULTIPLICACIÓN de los números {calc.n1} y {calc.n2} es: {round(calc.multip(),5)}")
print()
print(f"La DIVISIÓN de los números {calc.n1} y {calc.n2} es: {round(calc.divid(),5)}")
print()

