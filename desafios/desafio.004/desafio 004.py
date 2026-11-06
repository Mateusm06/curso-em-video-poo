from rich import print
import time 


class Livro:

    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(
            f"Você acabou de abrir o livro [blue]'{self.titulo}'[/blue] que tem {self.paginas} páginas no total, você está agora na página {self.pagina_atual}")

    def passar_pagina(self, quant_pag=1):
        cont = 0
        for pg in range(0, quant_pag, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} :arrow_forward: ", end="")
                time.sleep(0.2)
                cont += 1
            else:
                print(
                    "[red]Você chegou a última página do livro, não tem mais para onde avançar[/red]")
        print(f"Você avançou {cont} páginas e agora está na página {self.pagina_atual}")

    def fim_do_livro(self) -> bool:
        if self.pagina_atual == self.paginas:
            return True
        else:
            return False


l1 = Livro(titulo="Pai rico, Pai pobre", paginas=10)
l1.passar_pagina(5)
l1.passar_pagina(2)
l1.passar_pagina(2)
l1.passar_pagina(1)