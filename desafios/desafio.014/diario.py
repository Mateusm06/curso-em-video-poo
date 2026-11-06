class Diario:

    def __init__(self,senha = 'P@cY0'):
        self.__segredos = []
        self.__senha = senha

    def escrever(self,msg):
            if isinstance(msg,str) and len(msg) > 0:
                 self.__segredos.append(msg)
    
    def ler(self,senha = None):
        if senha != self.__senha:
             raise PermissionError("Senha inválida, você não pode ler meu diário")
        else:
            print("Diário liberado")
            for segredo in self.__segredos:
                 print(f"- {segredo}")
             
    @property
    def senha(self):
        raise PermissionError("Você não tem permissão para ver a senha")

    

    