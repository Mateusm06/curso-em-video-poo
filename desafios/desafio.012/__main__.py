from rich import inspect
from  personagem import *
def main():
    p1 = Guerreiro("Kratos",10000)
    p2 = Mago("Gandalf", 5000)
    p1.atacar(p2,1000)
    p2.curar()
if __name__ == "__main__":
    main()    