from hashlib import sha256

class Conta_bancaria:

    def __init__(self, id:int, nome:str, saldo:float, chave:str = None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode("utf-8")).hexdigest()

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self,novo_nome):
        chave = self.pede_senha()
        if self.validar_senha(chave): 
            if len (novo_nome) > 0:
                self._titular = novo_nome
                print(f"O nome do titular foi alterado para {novo_nome}")
        else:
            print("Senha incorreta") 








    def validar_senha(self,chave):
        if self.__hash == sha256(chave.encode("utf-8")).hexdigest():
            return True
        else:
            return False

    def pede_senha(self):

        from pwinput import pwinput

        while True:
            senha = str(pwinput("Digite a senha de 6 digitos: "))
            if len(senha) >= 6:
                break
        return senha

    def sacar(self,valor,chave = None):
        if chave is None:
            chave = self.pede_senha()
        if self.validar_senha(chave):
            valor = abs(valor)
            self.__saldo -= valor
            print(f"O saque no valor de {valor} foi autorizado, seu novo saldo é de {self.__saldo}")
        else:
            print("Saque indisponivel, senha incorreta")

    def depositar(self,valor):
        valor = abs(valor) 
        self.__saldo += valor
        print(f"Deposito de {valor} concluido com sucesso, seu novo saldo é {self.__saldo}")