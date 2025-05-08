#3. Implementa una clase 'Calculadora' con métodos para sumar, restar, multiplicar y dividir dos números.



class Calculadora:
    def sumar(self, num1, num2):
        return num1 + num2

    def restar(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2

    def dividir(self, num1, num2):
       
        if num2 == 0:
            return "Error: No se puede dividir por cero."
        else:
            return num1 / num2

mi_calculadora = Calculadora()

resultado_suma = mi_calculadora.sumar(5, 3)
print(f"5 + 3 = {resultado_suma}")

resultado_resta = mi_calculadora.restar(10, 4)
print(f"10 - 4 = {resultado_resta}")

resultado_multiplicacion = mi_calculadora.multiplicar(2, 7)
print(f"2 * 7 = {resultado_multiplicacion}")

resultado_division = mi_calculadora.dividir(9, 3)
print(f"9 / 3 = {resultado_division}")

resultado_division_cero = mi_calculadora.dividir(6, 0)
print(f"6 / 0 = {resultado_division_cero}")