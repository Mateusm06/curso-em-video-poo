class Carro:
    """Essa classe cria um carro que recebe atributos, como nome, modelo e ano """ # Doc String
    def __init__(self,nome,modelo,ano,marca,cor,combustivel): # Método Construtor
        # Atributos de instância
        self.nome = nome
        self.modelo = modelo
        self.ano = ano
        self.marca = marca
        self.cor = cor
        self.combustivel = combustivel

print(Carro.__doc__) # Dunder atribute (Dunder = Double Underline)