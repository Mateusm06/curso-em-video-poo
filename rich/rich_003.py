from rich import print
from rich.table import Table
# Comando para criar tabelas
tabela = Table(title="Tabela de preços")
tabela.add_column("Nome", justify="center")
tabela.add_column("Preço", justify="center", style="green")
tabela.add_row("Coca 2L", "R$ 10.00")
tabela.add_row("H20", "R$ 5.00")
print(tabela)