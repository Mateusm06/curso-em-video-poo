from transporte import Transporte


class Caminhao(Transporte):
    fator = 1.2

    def __init__(self, distancia):
        super().__init__(distancia)
        

    
    def calc_frete(self): 
        if self.distancia >= 50:
            self.frete = self.distancia * Caminhao.fator
            return f"R$ {self.frete:.2f}"
        
        else:
            self.frete = 0
            return(f":prohibited: [red] A distância informada é abaixo do limite mínimo para um {self.__class__.__name__}[/]")
           
