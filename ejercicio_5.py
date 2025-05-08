#5. Diseña una clase 'CuentaBancaria' con métodos para depositar, retirar y mostrar el saldo.

class Cuenta_Bancaria:
    
    def __init__(self,depositar,retirar,saldo):
        self.depositar = depositar
        self.retirar = retirar
        self.saldo = saldo
        
    def saldo_final(self):
        print(f"Hoy fui a depositar en el banco una suma de {self.depositar} y mañana ire a retirar {self.retirar} mi saldo final es {self.saldo}")
        
cuenta= Cuenta_Bancaria("1000 cordobas","650 cordobas","350 cordobas") 
        
print(cuenta.depositar,cuenta.retirar,cuenta.saldo)

cuenta.saldo_final()