from classes import *

def main():
    u = [Usuario("Renato", "renato123@gmail.com"),Usuario("Maria","maria789@hotmail.com")]
    a = [Aluno("Miguel","Arquitetura","2° ano"),Aluno("William", "Engenharia", "3° ano")]

    exportar_dados(XML(),u)
    exportar_dados(JSON(),a)
    
if __name__ in "__main__":
    main()