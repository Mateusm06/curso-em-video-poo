from pessoa import *
from rich import inspect


def main():

    a1 = Aluno("Mateus", 2002,"ADM")
    a1.add_curso("KKK")
    a1.curso = "KKK"
    inspect(a1, private=True, methods=True)


if __name__ in "__main__":
    main()
