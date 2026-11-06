from rich import print
from rich import inspect


class Funcionario:
    # Atributos de Classe
    empresa = ("Amazon")

    def __init__(self, nome, setor, cargo):
        # Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self) -> str:
        return (f"[green]Olá, meu nome é {self.nome} e sou {self.cargo} do setor de {self.setor} da {Funcionario.empresa}[/green]:handshake:")


func1 = Funcionario(nome="Pedro", setor="vendas", cargo="gerente")
func2 = Funcionario(nome="Raul", setor="marketing", cargo="encarregado")
print(func1.apresentar())
print(func2.apresentar())
