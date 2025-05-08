"""5. Diseña una clase 'CuentaBancaria' con métodos para depositar, retirar y mostrar
el saldo.
"""

import time
import os
limpia = os.system("cls")

limpia
class CuentaBancaria:
    def __init__(self):
        self.deposito = 0
        self.retiro = 0
        self.saldo = 0
    
    def monto(self):
        print(f"Su SALDO actual es {round(self.saldo,2)}")
        print(f"Haga un depósito para aumentar sus finanzas")
        
    def depo(self):
        a = input(print("¿Desea hacer un depósito? S/N "))
        if a.upper() == "S":
            self.deposito = float(input(print("Digite el monto a depositar: ")))
            self.saldo =+ self.deposito
            print()
            print(f"Su SALDO actual es de {self.saldo}")
            print()
        elif a.upper() == "N":
            print(f"Fue un placer atenderlo.  Hasta la próxima!!!")
            time.sleep(3)
            exit
        else:
            print("Opción incorrecta")
            print("Hasta Pronto")
            time.sleep(3)
            limpia
            exit
            
    def reti(self):
        print(f"Su saldo actual es de {self.saldo}")
        print()
        b = input(print("¿Desea hacer un retiro? S/N "))
        if b.upper() == "S":
            self.deposito = float(input(print("Digite el monto a retirar: ")))
            self.saldo =- self.deposito
            print()
            print(f"Su SALDO actual es de {self.saldo}")
            print()
        elif b.upper() == "N":
            print(f"Fue un placer atenderlo.  Hasta la próxima!!!")
            time.sleep(5)
            limpia
            exit
        else:
            print("Opción incorrecta")
            print("Hasta Pronto")
            time.sleep(5)
            limpia
            exit
            
ctaban = CuentaBancaria()
print(f"CUENTA BANCARIA")
print()
ctaban.monto()
ctaban.depo()
ctaban.reti
