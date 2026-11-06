from classes import Quadrado, Circulo


def main():
    q1 = Quadrado(10)
    c1 = Circulo(12)

    print(f"O perímetro desse polígono é de {q1.calculo_perimetro()}")

    print(f"A área desse polígono é de {q1.calculo_area()}")

    print(f"O perímetro desse polígono é de {c1.calculo_perimetro():.1f}")

    print(f"A área desse polígono é de {c1.calculo_area():.1f}")


if __name__ == "__main__":
    main()
