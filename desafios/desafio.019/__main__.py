from classes import *

def main():
    
    funcionarios = [Desenvolvedor("Manuel",5000),
                    Designer("Lucas",2500),
                    Gerente("Rodrigo", 8000)]

    funcionarios[0].salario = 6000 

    for f in funcionarios:
        print(f)

    
if __name__ in "__main__":
    main()