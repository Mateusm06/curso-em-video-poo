from rich import print
from rich.panel import Panel


class Gamer:

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos_fav = []

    def add_favoritos(self, jogos):
        self.jogos_fav.append(jogos)
        self.jogos_fav = sorted(self.jogos_fav, key=str.lower)

    def mostrar_ficha(self):
        conteudo = (f'Nome real: [black on purple]{self.nome}[/]')
        conteudo += ('\nJogos favoritos:')
        for jogo in self.jogos_fav:
            conteudo += (f"\n:video_game:  [purple]{jogo}[/]")
        mensagem = Panel(conteudo,width=34 , title=(f'Jogador <{self.nick}>'))
        print(mensagem)


j1 = Gamer(nome="Mateus", nick="Seunick")
j1.add_favoritos("Counter Strike 2")
j1.add_favoritos("FIFA")
j1.add_favoritos("Red Dead Redemption 2")
j1.mostrar_ficha()

j2 = Gamer(nome="Ricardo", nick="20matar70correr")
j2.add_favoritos("Dota 2")
j2.add_favoritos("Overwatch")
j2.add_favoritos("God Of War")
j2.mostrar_ficha()