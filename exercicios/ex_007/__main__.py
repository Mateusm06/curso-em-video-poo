from rich import inspect,print
from Classes import Aluno,Professor,Funcionario

def main():
    a1 = Aluno(nome="Pedro",idade=18,curso="Engenharia da Computação",turma="A")
    a1.fazer_matricula()
    a1.fazer_aniversario()
    a1.estudar()
    inspect(a1,methods=True)

    p1 = Professor("Euclerio",60,"Computação","Pós Graduado")
    p1.dar_aula()
    p1.estudar()
    inspect(p1,methods=True)

    f1 = Funcionario("Roberto",35,"Analista","Vendas")
    f1.bater_ponto()
    f1.estudar()
    inspect(f1,methods=True)

if __name__ == "__main__":
    main()