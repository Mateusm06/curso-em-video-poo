from abc import ABC, abstractmethod
import math

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados


    @abstractmethod
    def calculo_perimetro(self):
        pass


    @abstractmethod
    def calculo_area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado
        self.qtd_lados = 4


    def calculo_perimetro(self):
        return self.lado * self.qtd_lados
         

    def calculo_area(self):
        return self.lado ** 2
         

class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio
        self.qtd_lados = 0
    
    def calculo_perimetro(self):
        return math.pi * (2 * self.raio)
        

    def calculo_area(self):
        return math.pi * (self.raio ** 2)
        