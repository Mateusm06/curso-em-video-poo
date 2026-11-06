from abc import ABC,abstractmethod
from time import sleep


class Bebida_Quente(ABC):
  

    def preparar(self):
        print(f"--- Iniciando o Preparo do seu {self.__class__.__name__} ---")
        sleep(1)
        self.ferver_agua()
        sleep(1.5)
        self.misturar()
        sleep(1.5)
        self.servir()
        sleep(1)
        print("--- Bebida Pronta ---\n")


    def ferver_agua(self):
        print("1. Fervendo a água a 100 graus Celsius.")


    @abstractmethod
    def misturar(self):
        pass


    @abstractmethod
    def servir(self):
        pass


