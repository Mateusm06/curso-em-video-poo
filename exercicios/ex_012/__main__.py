from classes import *
from rich import inspect

def main():
    
    a = Pato("Perry")
    b = Cachorro("Husky")
    c = Gato("Odin")
    d = Galinha("Jalo Jerônimo")
    e = Spitz("Little Spitz")
    f = Pitbull("Bira")

    print(a.emitir_som())
    print(b.emitir_som())
    print(c.emitir_som())
    print(d.emitir_som())
    print(e.emitir_som())
    print(f.emitir_som())

if __name__ in "__main__":
    main()