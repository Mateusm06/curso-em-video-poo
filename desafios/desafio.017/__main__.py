from conta_bancaria import *
from rich import inspect


def main():

    cc = Conta_bancaria(123, "Mateus", 20000,"admin1")
    cc.validar_senha("admin1")
    cc.depositar(5000)
    cc.sacar(2500)
    cc.nome = ("Marcos")
    inspect(cc, private=True, methods=True)


if __name__ in "__main__":
    main()
