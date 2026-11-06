from funcionario import *


def main():
    f1 = Funcionario_Mensalista("Ruan",9500)
    f1.analisar_sal()

    f2 = Funcionario_Horista("Paula",12,200)
    f2.analisar_sal()

if __name__ == "__main__":
    main()