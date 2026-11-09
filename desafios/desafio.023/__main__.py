from classes import *
from rich import inspect

def main():

    c1 = Carrinho()
    c2 = Carrinho()
    p1 = Produto("Mouse",650)
    p2 = Produto("Teclado",400)
    p3 = Produto("Monitor",1120)
    c1 += p1 
    c2 += p3
    print(c1.total)
    print(c2.total)
    c1 += c2
    print(c1.total)
    print(c1)
    print(c2)
    
if __name__ in "__main__":
    main()