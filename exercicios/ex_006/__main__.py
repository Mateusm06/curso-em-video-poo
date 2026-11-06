from rich import inspect,print
from Aluno import Aluno
from Professor import Professor
from Funcionario import Funcionario


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