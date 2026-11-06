from medidas import *
from rich import inspect

def main():
    r = Retangulo(5,8)
    r.base = 10
    r.altura = 7
    r.medidas = (9,6)
    print(r.medidas)
    inspect(r,private=True,methods=True)

if __name__ in "__main__":
    main()