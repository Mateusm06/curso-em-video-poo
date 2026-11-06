from transporte import Transporte

class Moto(Transporte):
    fator = 0.5


    def __init__(self, distancia):
        super().__init__(distancia)
        
    
    def calc_frete(self):
        self.frete = self.distancia * Moto.fator
        return f"R$ {self.frete:.2f}"