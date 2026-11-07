from classes import *
from rich import inspect


def main():

    a1 = PDF("A3", 250000)
    a2 = DOC("Contrato", 1300234)
    a3 = XLS("Planilha", 5000000)
    a1.abrir()
    a2.abrir()
    a3.abrir()


if __name__ in "__main__":
    main()
