from cafe import Cafe
from cha import Cha
from leite import Leite

def main():
    bebida1 = Cafe()
    bebida1.preparar()

    bebida2 = Cha()
    bebida2.preparar()

    bebida3 = Leite()
    bebida3.preparar()

if __name__ == "__main__":
    main()
