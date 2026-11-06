from rich import print
from rich.panel import Panel


class Controle_Remoto:
    canal_min = 1
    canal_max = 5
    volume_min = 1
    volume_max = 5

    def __init__(self, canal_atual, volume_atual):
        self.canal_atual = canal_atual
        self.volume_atual = volume_atual
        self.estado_aparelho = False

    def liga_desliga(self):
        self.estado_aparelho = not self.estado_aparelho

    def passar_canal(self):
        if self.estado_aparelho == True:
            if self.canal_atual == Controle_Remoto.canal_max:
                self.canal_atual = Controle_Remoto.canal_min
            else:
                self.canal_atual += 1

    def voltar_canal(self):
        if self.estado_aparelho == True:
            if self.canal_atual == Controle_Remoto.canal_min:
                self.canal_atual = Controle_Remoto.canal_max
            else:
                self.canal_atual -= 1

    def aumentar_volume(self):
        if self.estado_aparelho == True:
            if self.volume_atual != Controle_Remoto.volume_max:
                self.volume_atual += 1

    def diminuir_volume(self):
        if self.estado_aparelho == True:
            if self.volume_atual != Controle_Remoto.volume_min:
                self.volume_atual -= 1

    def mostrar_tela(self):
        if self.estado_aparelho == False:
            conteudo = f':prohibited: [red]A tv está desligada[/]'
        else:
            conteudo = f'Canal = '
            for canal in range(Controle_Remoto.canal_min, Controle_Remoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f' [yellow on yellow] {canal} [/]'
                else:
                    conteudo += f' {canal} '
            conteudo += f'\nVolume = '
            for volume in range(Controle_Remoto.volume_min, Controle_Remoto.volume_max + 1):
                if volume <= self.volume_atual:
                    conteudo += '[black on cyan] [/]'
                else:
                    conteudo += '[black on white] [/]'
        tv = Panel(conteudo, title="[ TV ]", width=30)
        print(tv)


tv1 = Controle_Remoto(canal_atual=1, volume_atual=1)

while True:
    tv1.mostrar_tela()
    comando = input(f"< CH {tv1.canal_atual} >  - VOL {tv1.volume_atual} + ")
    match comando:
        case "0":
            break
        case "@":
            tv1.liga_desliga()
        case "<":
            tv1.voltar_canal()
        case ">":
            tv1.passar_canal()
        case "-":
            tv1.diminuir_volume()
        case "+":
            tv1.aumentar_volume()
    print("\n" * 10)
