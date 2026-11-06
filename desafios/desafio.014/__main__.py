from diario import *
from rich import inspect

def main():

    d = Diario("admin")
    d.escrever("Teste")
    d.escrever("O Bahia é o mundo")
    d.ler("admin")
    #inspect(d,private=True,methods=True)



if __name__ in "__main__":
    main()