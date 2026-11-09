class Carrinho:

    def __init__(self,produtos:list = None):
        self.produtos = produtos if produtos else []

    @property
    def total(self):
         return sum(p.preço for p in self.produtos)

    def __str__(self):
             return f'Esse carrinho tem os produtos {self.produtos[0]}'

    def __iadd__(self, valor):
            if isinstance(valor,Produto):
                return Carrinho(self.produtos + [valor])
            elif isinstance(valor,Carrinho):
                 return Carrinho(self.produtos + valor.produtos)
            else:
                 raise TypeError("Você tentou adicionar algo inválido ao carrinho")

    def __str__(self):
             itens = ", ".join(str(p) for p in self.produtos)

             return f'Esse carrinho tem os produtos {itens} e o total dele é de {formatar_dinheiro(self.total)}'
            

class Produto:
    def __init__(self,nome:str = "", preço:float = 0):
        self.nome = nome    
        self.preço = preço

    def __str__(self):
        return f'{self.nome}({formatar_dinheiro(self.preço)})'

def formatar_dinheiro(valor:float):
    import locale
    locale.setlocale(locale.LC_ALL,"pt-BR.UTF-8")
    return locale.currency(valor,grouping=True)