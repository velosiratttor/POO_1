class CuentaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, cantidad):
        self.saldo += cantidad
        print("Depósito realizado.")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print("Retiro realizado.")
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        print("Saldo actual:", self.saldo)

cuenta = CuentaBancaria()
cuenta.depositar(500)
cuenta.retirar(30)
cuenta.mostrar_saldo()

