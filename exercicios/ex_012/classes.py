from abc import ABC,abstractmethod

class Animais(ABC):
    def __init__(self,nome:str = ""):
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
            pass


class Pato(Animais):
    def __init__(self, nome = ""):
        super().__init__(nome)

    def emitir_som(self):
        return f"{self.nome} acabou de dizer 'QUACK! QUACK!'"

class Cachorro(Animais):
    def __init__(self, nome = ""):
        super().__init__(nome)

    def emitir_som(self):
        return f"{self.nome} acabou de dizer 'AU! AU!'"


class Spitz(Cachorro):
    def __init__(self, nome=""):
        super().__init__(nome)

    def emitir_som(self):
        return f"{self.nome} acabou de dizer 'WOOF! WOOF! WOOF!'"


class Pitbull(Cachorro):
    def __init__(self, nome=""):
        super().__init__(nome)

    def emitir_som(self):
        return f"{self.nome} acabou de dizer 'RUF! RUF! RUF!'"

class Gato(Animais):
    def __init__(self, nome = ""):
        super().__init__(nome)

    def emitir_som(self):
        return f"{self.nome} acabou de dizer 'MIAU! MIAU!'"


class Galinha(Animais):
    def __init__(self, nome = ""):
        super().__init__(nome)  

    def emitir_som(self):
        return f"{self.nome} acabou de dizer 'PÓ! PÓ!'"