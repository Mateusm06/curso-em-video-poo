# Criando classe
class Conta_bancaria:
    """ Cria uma conta bancária e permite fazer saques e depósitos"""

    def __init__(self, numero_conta, nome_titular, saldo_conta):
        self.numero_conta = numero_conta
        self._nome_titular = nome_titular
        self.__saldo_conta = saldo_conta

# Criando métodos

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo_conta += valor
        print(
            f"O valor de R$ {valor:,.2f} foi depositado na sua conta, seu novo saldo é de R$ {self.__saldo_conta:,.2f}")

    def sacar(self, valor):
        valor = abs(valor)
        if self.__saldo_conta > valor:
            self.__saldo_conta -= valor
            print(
                f"O valor de R$ {valor:.2f} foi sacado com sucesso, seu novo saldo é de R$ {self.__saldo_conta:,.2f}")
        else:
            print(
                f"Saque no valor de R$ {valor:.2f} negado! Saldo insuficiente")

    def __str__(self):
        #return (f"A conta de número {self.numero_conta} é de {self._nome_titular} e tem R$ {self.__saldo_conta:,.2f} de saldo")
        return (f"Estado atual da conta: {self.__dict__}") 


