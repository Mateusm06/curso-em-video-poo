from abc import ABC,abstractmethod
import random
from rich import print

class Personagem(ABC):

    def __init__(self,nome,vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self,alvo,força):

        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0,len(self.golpes))]
            print(f"{self.nome} atacou {alvo.nome} com um {golpe}")
            alvo.receber_dano(força)
        else: 
            print(f"O ataque {self.nome} -> {alvo.nome} não pode acontecer")

    def receber_dano(self,dano):
        fator = random.randint(0,dano)
        self.vida -= fator 
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu [red]dano de {fator}[/] e ficou com {self.vida} pontos de vida")

    @abstractmethod 
    def curar():
        pass


class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Cotovelada Giratória", "Golpe de Machado", "Chute Alto"]

    def curar(self):
        fator = random.randint(0,2000)
        self.vida += fator
        print(f"O {self.nome} enrolou uma atadura no braço e recuperou {fator} pontos de vida")

class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Chuva de Meteoros", "Raio Paralizante", "Bola de Fogo"]

    def curar(self):
        fator = random.randint(0,5000)
        self.vida += fator
        print(f"O {self.nome} usou uma magia de cura e recuperou {fator} pontos de vida")
    
