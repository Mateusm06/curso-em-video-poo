from rich import print
from rich.panel import Panel
class Produto:
    def __init__(self,nome,preço):
        self.nome = nome
        self.preço = preço

    def etiquetar(self):
        conteudo = f"{self.nome.center(30," ")}"
        conteudo += f"{"-" * 30}"
        precof = f"R$ {self.preço:,.2f}"
        conteudo += f"{precof.center(30,".")}"
        etiqueta = Panel(conteudo,width=34,title="Produto")
        print(etiqueta)

p1 = Produto(nome="Macbook", preço=12000)
p2 = Produto(nome="Playstation 5", preço=5400)
p1.etiquetar()
p2.etiquetar()