from abc import ABC,abstractmethod #Abstract base classes

class Pessoa(ABC):
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar():
        pass


class Aluno(Pessoa):
    def __init__(self,nome,idade,curso,turma):
        super().__init__(nome,idade)
        self.curso = curso
        self.turma = turma
        
    def fazer_matricula(self):
        print(f"O aluno {self.nome} acabou de se matricular")

    def estudar(self):
        print(f"{self.nome} está estudando {self.curso} na turma {self.turma} ")


class Professor(Pessoa):
    def __init__(self,nome,idade,especialidade,nivel):
        super().__init__(nome,idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"O professor {self.nome} acabou de começar a sua aula")

    def estudar(self):
        print(f"{self.nome} é especialista em {self.especialidade} e está estudando para {self.nivel}")


class Funcionario(Pessoa):
    def __init__(self,nome,idade,cargo,setor):
        super().__init__(nome,idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"O funcionário {self.nome} acabou de bater o ponto")

    def estudar(self):
        print(f"{self.nome} está se especializando na área de {self.setor}")