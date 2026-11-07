from classes import *
from rich import inspect


def main():

    p1 = Boleto()
    p2 = Pix()
    p3 = Cartao_Credito()

    # p1.pagar(550)
    # p2.pagar(8750)
    # p3.pagar(2223.54)
    finalizar_compra(p1, 550)
    finalizar_compra(p2,800)


if __name__ in "__main__":
    main()
