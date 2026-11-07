class Mae:
    def __init__(self,nome:str = ""):
        self.nome = nome

    def fazer_pudim(self):
        print(f"{self.nome} faz pudim com leite condensado e calda")

    def fritar_coxinha(self):
        print(f"{self.nome} frita coxinha no óleo de soja")

class filha(Mae):

    def fazer_pudim(self):
        print(f'{self.nome} faz pudim com nutella')



class filho(Mae):

    def fritar_coxinha(self):
        print(f"{self.nome} frita coxinha na airfryer")