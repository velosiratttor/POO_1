#                                      Cuenta de Cliente 
#Crea una clase CuentaCliente con el nombre del cliente y su balance. Implementa
#métodos para depositar y retirar dinero, usando propiedades para controlar el
#acceso al balance. Evita retiros que excedan el saldo. 


class Cuenta_Cliente:
    def __init__(self,nombre_cliente,balance):
        self.nombre = nombre_cliente
        self.__balance = balance
        
    def depositar(self,cantidad):
        if cantidad >= self.__balance:
            self.__balance += cantidad
            print("El deposito es de ",self.__balance)
        else:
            print("Deposito = ",self.__balance)
        
    def retiro(self,retiro):    
        if retiro <= self.__balance:
            self.__balance -= retiro
            print("El retiro es de ",self.__balance)
        else:
            print("Fondos insuficientes.")

cliente = Cuenta_Cliente("Samuel",500)

print(cliente.nombre)
cliente.depositar(5000)
cliente.retiro(1000)