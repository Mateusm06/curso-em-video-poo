class Termostato:

    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self,nova_temperatura):

        if 16 <= nova_temperatura <= 30 and nova_temperatura % 0.5  == 0:
            self.__temperatura = nova_temperatura

        elif nova_temperatura < 16:
            self.temperatura = 16

        elif nova_temperatura > 30:
            self.temperatura = 30

        else:
           raise ValueError("Temperatura inválida")

    @property
    def ftemperatura(self):
        return (f"{self.temperatura}° Celsius")