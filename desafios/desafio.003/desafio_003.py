from rich import print
from rich.panel import Panel

class Churrasco:

    unidade_carne:float = 0.4
    preço_kg:float = 82.4

    def __init__(self, quant_pessoa, titulo,):
        self.quant_pessoa = quant_pessoa
        self.titulo = titulo

    def calcular_quant_carne(self) -> float:
        return self.quant_pessoa * Churrasco.unidade_carne

    def calcular_custo_total(self) -> float:
        return self.calcular_quant_carne() * self.preço_kg
    
    def calcular_custo_pessoa(self) -> float:
        return self.calcular_custo_total() / self.quant_pessoa

    def calcular(self):
        conteudo = f"Calculando o valor do {self.titulo} com {self.quant_pessoa} pessoas"
        conteudo += f"\nA quantidade de carne comprada foi de {self.calcular_quant_carne()} KG para que cada pessoa possa comer cerca de {Churrasco.unidade_carne * 1000} gramas"
        conteudo += f"\nO custo total foi de R$ {self.calcular_custo_total():,.2f} e o valor por pessoa foi de R$ {self.calcular_custo_pessoa():,.2f}"
        conteudo += f"\n[green]Manda o pix[/green] :zany_face:"
        tabela_preco = Panel(conteudo, title=self.titulo)
        print(tabela_preco)


c1 = Churrasco(titulo="Churrasco da galera", quant_pessoa=20)
c1.calcular()
