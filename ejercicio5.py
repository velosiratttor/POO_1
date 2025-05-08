#5. Diseña una clase 'CuentaBancaria' con métodos para depositar, retirar y mostrar el saldo.

class cuenta_bancaria:
    
    def __init__(self , nombre , ahorro):
        self.nombre = nombre
        self.ahorro = ahorro
    
    def depositar(self , deposito):
        return f'Su cuenta es de: {self.ahorro} monto a depositar es {deposito} en total {self.ahorro + deposito}'
    
    def retirar(self , retiro):
        return f'Su cuenta es de: {self.ahorro}  monto a retirar es {retiro} en total {self.ahorro - retiro}'
    
    def mostrar (self):
        return f'Nombre {self.nombre} , Cuenta: {self.ahorro}'

cuenta_bancaria1 = cuenta_bancaria('Lafise', 2500)

print(cuenta_bancaria1.depositar(300))