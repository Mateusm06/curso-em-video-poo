class Numero:

    def __init__(self,valor: int|float = 0):
        self.valor = valor

    def dobrar(self):
        self.valor = self.valor * 2

    def __str__(self):
        return f'Tenho o número {self.valor} dentro do número'

class Texto:

    def __init__(self,txt:str = ''):
        self.txt = txt
        
    def dobrar(self):
        self.txt = self.txt + self.txt

    def __str__(self):
            return f'Tenho o texto {self.txt} dentro do texto'    

class Lista:

    def __init__(self,lista:list = []):
        self.valores = lista

    def dobrar(self):
        self.valores = self.valores + self.valores

    def __str__(self):
            return f'Tenho os valores {self.valores} dentro da lista'
    
class Papel:

    def __init__(self):
        self.dobrado = False
        
    def dobrar(self):
        self.dobrado = True

    def __str__(self):
            return f'O papel está {'novo' if not self.dobrado else 'dobrado'}'
    
class Casa:
    def __init__(self):
        pass

    def __str__(self):
            return f'Casa'


def tente_dobrar(objeto):
    try:
        objeto.dobrar()
    except:
        print(f"O objeto {objeto} não pode ser dobrado")