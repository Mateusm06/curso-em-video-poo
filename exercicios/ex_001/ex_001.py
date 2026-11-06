# Criando classe

class Carro:
    def __init__(self): # Método Construtor
        # Atributos de instância
        self.nome = ''
        self.modelo = ''
        self.ano = 0
        self.marca = ''
        self.cor = ''
        self.combustivel = ''

# Criando Métodos

    def abastecer(self):
        if self.combustivel == "Gasolina":
            print(f"O seu {self.nome} está sendo abastecido")
        else:
            print(f"O seu carro não pode ser abastecido, pois ele não utiliza gasolina como combustivel")
    def mensagem(self):
        print(f"O seu carro é um {self.nome} {self.cor} da marca {self.marca}, ano {self.ano}")

# Criando objetos

Creta = Carro()
# Atributos do objeto
Creta.nome = "Creta"
Creta.modelo = "SUV"
Creta.ano = "2022"
Creta.marca = "Hyundai"
Creta.cor = "Cinza"
Creta.combustivel = "Gasolina"

# Chamando Métodos
Creta.mensagem()
Creta.abastecer()

Etios = Carro()
# Atributos do objeto
Etios.nome = "Etios"
Etios.modelo = "Hatch"
Etios.ano = "2019"
Etios.marca = "Toyota"
Etios.cor = "Branco"
Etios.combustivel = "Gasolina"

# Chamando Métodos
Etios.mensagem()
Etios.abastecer()


Seal = Carro()
# Atributos do objeto
Seal.nome = "Seal"
Seal.modelo = "Sedan"
Seal.ano = "2026"
Seal.marca = "BYD"
Seal.cor = "Preto"
Seal.combustivel = "Elétrico"

# Chamando Métodos
Seal.mensagem()
Seal.abastecer()