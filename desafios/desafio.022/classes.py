from rich.panel import Panel
from rich import print 
import emoji

class Mensagem:
    def __init__(self,mensagem:str = "",icone:str = ":thought_balloon:",tipo:str = "AVISO"):
        self._mensagem = mensagem
        self._icone = icone
        self._tipo = tipo

    def mostrar(self):
        painel = Panel(f"{self._mensagem}",title=f"{self._icone} {self._tipo} {self._icone}",width=35,style="white on black")
        print(painel)

class Erro(Mensagem):

    def __init__(self, mensagem = ""):
        super().__init__(mensagem, ":prohibited:", "Erro")
        
    def mostrar(self):
        painel = Panel(f"{self._mensagem}",title=f"{self._icone} {self._tipo} {self._icone}",width=35,style="red")
        print(painel)

class Alerta(Mensagem):

    def __init__(self, mensagem = ""):
        super().__init__(mensagem, ":warning:","AVISO" )

    def mostrar(self):
        painel = Panel(f"{self._mensagem}",title=f"{self._icone} {self._tipo} {self._icone}",width=35,style="yellow")
        print(painel)