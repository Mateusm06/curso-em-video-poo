from rich import print

print("-" * 30, "[purple]CALCULADORA[/]","-" * 30)

while True:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    escolha = int(input("Escolha qual operação deseja realizar:\n" \
    "[1] Adição\n" \
    "[2] Subtração\n" \
    "[3] Multiplicação\n" \
    "[4] Divisão "))
    resultado = 0
    match escolha:
        case 1:
            resultado = n1 + n2
        case 2:
            resultado = n1 - n2
        case 3:
            resultado = n1 * n2
        case 4:
            resultado = n1 / n2
    print(resultado)
    continue