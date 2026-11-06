from moto import Moto
from caminhao import Caminhao
from drone import Drone
from rich import print
from rich.table import Table

distancia = 80

viagem = [Moto(distancia), Caminhao(distancia), Drone(distancia)]

tabela = Table(title="Tabela de Fretes")
tabela.add_column("Distância")
tabela.add_column("Tipo")
tabela.add_column("Frete")

for item in viagem:
    tabela.add_row(f"{distancia} km",f"{type(item).__name__}",f"{item.calc_frete()}")

print(tabela)