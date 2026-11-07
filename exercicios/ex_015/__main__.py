from classes import *


def main():

    c1 = Carteira(1000)
    c2 = Carteira(1000)
    print(c1 == c2)

    c1 += 200
    c1 -= 100
    print(c1)

    c2 += 100

    if c1 == c2:
        print("Vocês tem o mesmo valor na carteira")
    elif c1 < c2:
        print("A segunda carteira tem mais dinheiro")
    else:
        print("A primeira carteira tem mais dinheiro")


if __name__ == "__main__":
    main()
