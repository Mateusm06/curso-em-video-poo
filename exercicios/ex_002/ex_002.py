# Criando classe

class Carro:
    def __init__(self,nome,modelo,ano,marca,cor,combustivel): # Método Construtor
        # Atributos de instância
        self.nome = nome
        self.modelo = modelo
        self.ano = ano
        self.marca = marca
        self.cor = cor
        self.combustivel = combustivel

# Criando Métodos

    def abastecer(self):
        if self.combustivel == "Gasolina":
            print(f"O seu {self.nome} está sendo abastecido")
        else:
            print(f"O seu {self.nome} não pode ser abastecido, pois ele não utiliza gasolina como combustivel")
    def __str__(self): # Dunder Method
        return (f"O seu carro é um {self.nome} {self.cor} da marca {self.marca}, ano {self.ano}")

# Criando objetos
Creta = Carro(nome="Creta", modelo="SUV", ano=2022, marca="Hyundai",cor="Cinza",combustivel="Gasolina") # Atributos do objeto

# Chamando Métodos
print(Creta)
Creta.abastecer()

Etios = Carro(nome="Etios", modelo="Hatch", ano=2019, marca="Toyota",cor="Branco",combustivel="Gasolina") # Atributos do objeto

# Chamando Métodos
print(Etios)
Etios.abastecer()

Seal = Carro(nome="Seal", modelo="Sedan", ano=2026, marca="BYD",cor="Preto",combustivel="Elétrico") # Atributos do objeto

# Chamando Métodos
print(Seal)
Seal.abastecer()

# Dunder atribute e dunder method para puxar um dicionário

print(Creta.__dict__) # Não Personalizável
print(Creta.__getstate__()) # Personalizável

# Dunder Atribute para descobrir classe

print(Creta.__class__)