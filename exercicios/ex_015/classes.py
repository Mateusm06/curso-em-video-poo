class Carteira:

    def __init__(self,valor:int|float = 0):
        self.__saldo = valor

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self,valor):
        raise PermissionError("Você não tem permissão para alterar esse saldo")

    def __str__(self):
        return f'Você tem R$ {self.__saldo:,.2f} na sua carteira'

    # Torna possível comparar 2 objetos
    def __eq__(self, other):
        if self.__saldo == other.__saldo:
            return True
        else:
            return False

    # Torna possível somar um valor ao objeto
    def __iadd__(self, valor:int|float):
        self.__saldo += valor
        return self

    # Torna possível subtrair um valor do objeto
    def __isub__(self, valor:int|float):
        self.__saldo -= valor
        return self

    # Torna possível comparar qual objeto tem o menor valor
    def __lt__(self, other):
        if self.__saldo <= other.__saldo:
            return True
        else:
            return False