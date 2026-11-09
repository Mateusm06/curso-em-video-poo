from abc import ABC,abstractmethod
import re 

class Validador(ABC):
    
    @abstractmethod
    def validar(self,valor:str):
        pass

class Usuario(Validador): # 5 a 20 caracteres, n pode ter maiusculas, pode ter numeros, pode ter _
    
    def validar(self,valor:str) -> bool: 

        regex = r"^[a-z0-9_]{5,20}$"
        if re.fullmatch(regex,valor):
            return True
        else: 
            return False

class Email(Validador): # - Deva contar uma única @, Usuário pode conter letras, números e alguns simbolos, Os dominios contém pontos, O TLD encerra com ponto e pelo menos 2 letras
    
    def validar(self,valor:str) -> bool: 
        regex = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z0-9]{2,}$"
        if re.fullmatch(regex,valor):
            return True
        else: 
            return False

class Senha(Validador): # Pelo menos 8 caracteres, Pelo menos uma minuscula e 1 maiúscula, Pelo menos um simbolo
    
    def validar(self,valor:str) -> bool: 
        regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@!#$%?]).{8,}$"
        if re.fullmatch(regex,valor):
            return True
        else: 
            return False


def validar_dado(validador:Validador, valor:str):
    resultado = validador.validar(valor)
    print(f"Valor: {valor} é valido? {'Sim' if resultado else 'Não'}")