from rich import print
from rich.panel import Panel
# Comando para criar paineis com mensagens
caixa = Panel("[purple]Esse aqui é um painel de exemplo[/purple] :+1:", title="Mensagem", style="red")

print(caixa)