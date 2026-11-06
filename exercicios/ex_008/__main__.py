from ex_008 import *
# Quando só nome do objeto ele é público, se tiver _ ele é protegido e se tiver __ ele é privado

def main():
    cliente1 = Conta_bancaria(nome_titular="Marcos",
                              numero_conta=1558962, saldo_conta=18750.35)
    cliente1.depositar(5000)
    cliente1.sacar(3000)
    cliente1.saldo = 0
    print(cliente1)

if __name__ == "__main__":
    main()
