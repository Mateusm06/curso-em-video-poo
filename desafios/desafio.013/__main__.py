from termostato import *
from rich import inspect


def main():
    t = Termostato()
    t.temperatura = 25
    print(f"A temperatura atual é de {t.temperatura}")
    inspect(t, private=True)


if __name__ == "__main__":
    main()
