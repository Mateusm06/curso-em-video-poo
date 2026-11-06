from credencial import *

def main():

    c = Credencial()
    c.senha = "admin"
    print(c.senha)
    c.validar("admin")
    c.validar("12345")
    
if __name__ in "__main__":
    main()