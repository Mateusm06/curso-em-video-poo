from rich import inspect,print


class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self,nome,idade,curso,turma):
        super().__init__(nome,idade)
        self.curso = curso
        self.turma = turma
        
    def fazer_matricula(self):
        print(f"O aluno {self.nome} acabou de se matricular")

class Professor(Pessoa):
    def __init__(self,nome,idade,especialidade,nivel):
        super().__init__(nome,idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"O professor {self.nome} acabou de começar a sua aula")

class Funcionario(Pessoa):
    def __init__(self,nome,idade,cargo,setor):
        super().__init__(nome,idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"O funcionário {self.nome} acabou de bater o ponto")

a1 = Aluno(nome="Pedro",idade=18,curso="Engenharia da Computação",turma="A")
a1.fazer_matricula()
a1.fazer_aniversario()
inspect(a1,methods=True)

p1 = Professor("Euclerio",60,"Computação","Pós Graduado")
p1.dar_aula()
inspect(p1,methods=True)

f1 = Funcionario("Roberto",35,"Analista","Vendas")
f1.bater_ponto()
inspect(f1,methods=True)