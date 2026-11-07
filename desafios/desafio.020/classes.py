from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self, extensao:str, nome:str = "", tamanho: int = 0):
        self.nome = nome
        self._extensao = extensao
        self.tamanho = tamanho/1000000
        self.extensao = extensao

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self,ext:str):
        formatos = ['pdf', 'doc', 'docx', 'xls','xlsx']
        ext = ext.lower().strip()
        if ext in formatos:
            self._extensao = ext
        else:
            raise AttributeError("O arquivo está em um formato não suportado")

    @property
    def nome_completo(self):
        return f"'{self.nome}.{self.extensao}' ({self.tamanho})"
   
    @abstractmethod
    def abrir(self):
        pass


class PDF(Arquivo):

    def __init__(self, nome = "", tamanho = 0):
        super().__init__("pdf", nome, tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} MB no Adobe Reader")
        
class DOC(Arquivo):

    def __init__(self, nome = "", tamanho = 0):
        super().__init__("docx", nome, tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} MB no Microsoft Word")
        

class XLS(Arquivo):

    def __init__(self, nome = "", tamanho = 0):
        super().__init__("xlsx", nome, tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} MB no Microsoft Excel")
        