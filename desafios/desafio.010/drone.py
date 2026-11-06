from transporte import Transporte


class Drone(Transporte):
    fator = 9.5
    def __init__(self, distancia):
        super().__init__(distancia)
        

    
    def calc_frete(self):   
        if self.distancia <= 10:
            self.frete = self.distancia * Drone.fator
            return self.frete
        else:
            self.frete = 0
            return(f":prohibited: [red] A distância informada é acima do limite mínimo para um {self.__class__.__name__}[/]")