# Diseña una clase 'CuentaBancaria' con métodos para depositar, retirar y mostrar el saldo.

class Cuenta_bancaria:
    def __init__(self,deposita,retira,saldo):
        self.deposita = deposita
        self.retira = retira
        self.saldo = saldo
        
    def depositar_1(self):
        desposita = 0
        return desposita + (self.deposita)
    
    def retiran_1(self):
        retira = 0
        return retira - (self.retira)
    
    def saldoss(self):
        saldo = 0
        return saldo + (self.saldo)
    
mi_cuenta = Cuenta_bancaria(10000,4000,6000)

print(f"Depositaste,",mi_cuenta.depositar_1())
print(f"Retirar,",mi_cuenta.retiran_1())
print(f"Saldo en el que encuentra su cuenta",mi_cuenta.saldoss())