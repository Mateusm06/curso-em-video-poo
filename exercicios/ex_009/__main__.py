from ex_009 import *
from rich import print, inspect


def main():

    av1 = Avaliacao("Mateus", "Matemática")
    av1.set_nota(10)
    print(f"{av1.nome} tirou nota {av1.get_nota()} na prova de {av1.disciplina}")
    inspect(av1,private=True)


if __name__ == "__main__":
    main()
