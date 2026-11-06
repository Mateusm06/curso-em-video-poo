from abc import ABC,abstractmethod
from rich.panel import Panel
from rich import print


class Funcionario(ABC):
    sal_minimo = 1612
    inss = 7.5


    def __init__(self,nome,sal_bruto):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0

    
    def analisar_sal(self):
        conteudo = (f"O salário de [blue]{self.nome}[/][purple] ({self.__class__.__name__})[/] é de [green]R$ {self.calc_sal():.2f}[/] e corresponde a [yellow]{self.salario/self.sal_minimo:.1f} salários mínimos[/]")
        painel = Panel(conteudo,title="Análise de Salários",width=40)
        print(painel)


    @abstractmethod
    def calc_sal(self):
        pass
        

class Funcionario_Horista(Funcionario):


    def __init__(self, nome, valor_hora,horas_trab):
        super().__init__(nome,0)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab


    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.horas_trab
        self.salario = self.sal_bruto - (self.sal_bruto * (Funcionario_Mensalista.inss/100))
        return self.salario


class Funcionario_Mensalista(Funcionario):


    def __init__(self, nome, sal_bruto = Funcionario.sal_minimo):
        super().__init__(nome,sal_bruto)
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * (Funcionario.inss/100)) 
        return self.salario


