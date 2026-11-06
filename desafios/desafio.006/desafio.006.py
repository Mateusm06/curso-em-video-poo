from rich import print


class Caneta:
    def __init__(self, cor="azul"):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "blue"
            case "verde":
                escolha = "green"
            case "vermelha" | "vermelho":
                escolha = "red"
            case _:
                escolha = "white"
        self.cor = escolha
        self.tampada = True

    def destampar(self):
        print(f"A caneta {self.cor} foi destampada")
        self.tampada = False

    def tampar(self):
        print(f"A caneta {self.cor} foi tampada")
        self.tampada = True

    def escrever(self, frase):
        if self.tampada == False:
            print(f"[{self.cor}]{frase}[/]",end='')
        else:
            print(f"A caneta {self.cor} precisa ser destampada primeiro")

    def quebrar_linha(self, qtd_linhas):
        print('\n' * qtd_linhas)


c1 = Caneta(cor="Azul")
c2 = Caneta(cor="Verde")
c3 = Caneta(cor="Vermelha")

c1.destampar()
c1.escrever("Teste")
c1.quebrar_linha(2)
c2.destampar()
c2.escrever("Teste")
c2.quebrar_linha(1)
c3.escrever("Teste")
c3.destampar()
c3.quebrar_linha(1)
c3.escrever("E agora?")
