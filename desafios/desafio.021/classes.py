from abc import ABC,abstractmethod
import locale

class Pagamento(ABC):

    def __init__(self):
        self._valor = None

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self,valor:float):
        if valor > 0:
            self._valor = valor 
        else:
            raise ValueError("O pagamento só pode ser efetuado para valores positivos")

    @property
    def fvalor(self):
        locale.setlocale(locale.LC_ALL,locale="pt-BR.UTF-8")
        return locale.currency(self._valor,grouping=True)

    @abstractmethod
    def pagar(self,valor:float):
        pass


class Boleto(Pagamento):

    def pagar(self, valor:float):
        if valor > 0:
            try:
                self.valor = valor
                print(f"O valor de {self.fvalor} foi pago no {self.__class__.__name__}")
            except Exception as e:
                print(f"Falha no pagamento de {self.fvalor} via {self.__class__.__name__}")
        else:
            raise ValueError("Você não pode pagar um valor negativo")

class Pix(Pagamento):

    def pagar(self,valor:float):
        if valor > 0:
            try:
                self.valor = valor
                print(f"O valor de {self.fvalor} foi pago no {self.__class__.__name__}")
            except Exception as e:
                print(f"Falha no pagamento de {self.fvalor} via {self.__class__.__name__}")
        else:
            raise ValueError("Você não pode pagar um valor negativo")
        

class Cartao_Credito(Pagamento):

    def pagar(self,valor:float):
        if valor > 0:
            try:
                self.valor = valor
                print(f"O valor de {self.fvalor} foi pago no {self.__class__.__name__}")
            except Exception as e:
                print(f"Falha no pagamento de {self.fvalor} via {self.__class__.__name__}")
        else:
            raise ValueError("Você não pode pagar um valor negativo")
            
def finalizar_compra(tipo_pag:Pagamento,valor:float):

    return tipo_pag.pagar(valor)