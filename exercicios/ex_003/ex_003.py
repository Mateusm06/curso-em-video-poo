# Criando classe
class Conta_bancaria:
    """ Cria uma conta bancária e permite fazer saques e depósitos"""

    def __init__(self, numero_conta, nome_titular, saldo_conta):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo_conta = saldo_conta

# Criando métodos

    def depositar(self, valor):
        self.saldo_conta += valor
        print(
            f"O valor de R$ {valor:,.2f} foi depositado na sua conta, seu novo saldo é de R$ {self.saldo_conta:,.2f}")

    def sacar(self, valor):
        if self.saldo_conta > valor:
            self.saldo_conta -= valor
            print(
                f"O valor de R$ {valor:.2f} foi sacado com sucesso, seu novo saldo é de R$ {self.saldo_conta:,.2f}")
        else:
            print(
                f"Saque no valor de R$ {valor:.2f} negado! Saldo insuficiente")

    def __str__(self):
        return (f"A conta de número {self.numero_conta} é de {self.nome_titular} e tem R$ {self.saldo_conta:,.2f} de saldo")


cliente1 = Conta_bancaria(nome_titular="Marcos",
                          numero_conta=1558962, saldo_conta=18750.35)

cliente1.depositar(5000)
cliente1.sacar(3000)
