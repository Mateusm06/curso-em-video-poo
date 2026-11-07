from abc import ABC,abstractmethod

class Funcionario(ABC):
    def __init__(self,nome:str = "", salario:float = 1621):
        self.nome = nome
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self,valor:float = None):
        if valor == None:
            raise PermissionError("Não é possível alterar o salário desse jeito")
        if valor >= self.__salario:
            self.__salario = valor
        else:
            raise ValueError("Você não pode reduzir o salário de um funcionário")

    def __str__(self):
        return f'{self.nome} ganha R$ {self.__salario:,.2f} e por ser {self.__class__.__name__} o bônus será de R$ {self.calcular_bonus():,.2f}  '

    @abstractmethod
    def calcular_bonus(self):
        pass

class Gerente(Funcionario): 

    def calcular_bonus(self): # Bônus de 15%
        bonus = self.salario * 0.15
        return bonus

class Designer(Funcionario): 

    def calcular_bonus(self): # Bônus de 8%
        bonus = self.salario * 0.8
        return bonus



class Desenvolvedor(Funcionario): 

    def calcular_bonus(self): # Bônus de 10%
        bonus = self.salario * 0.10
        return bonus