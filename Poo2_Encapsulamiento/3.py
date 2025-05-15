#Crea una clase CuentaCliente con el nombre del cliente y su balance.
#Implementa  métodos para depositar y retirar dinero, 
#usando propiedades para controlar el  acceso al balance.
#Evita retiros que excedan el saldo. 
class CuentaCliente:
    def __init__(self, nombre, balance):
        self.nombre = nombre
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__balance += cantidad
        else:
            print("Error: El depósito debe ser mayor que cero.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__balance:
            self.__balance -= cantidad
        else:
            print("Error: Fondos insuficientes o cantidad inválida.")


cuenta = CuentaCliente("Luis", 500)
cuenta.depositar(200)
cuenta.retirar(100)
cuenta.retirar(700)  
print(cuenta.balance)
