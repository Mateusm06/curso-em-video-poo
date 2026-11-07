class Porta:
    def abrir(self):
        print("Gire a maçaneta e empurre a porta")

class Empresa:
    def abrir(self):
        print("Vá até o site do empreendedor com a documentação necessária")

class Ovo:
    def abrir(self):
        print("Quebre a casca com uma colher")


class Pedra:
    pass


# Método pythonico polimorfico duck typing
def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f"O objeto do tipo {objeto.__class__.__name__} não pode ser aberto")