class Retangulo:
    def __init__(self,base,altura):
        self._base = None
        self._altura = None
        self._area = None
        self.base = base
        self.altura = altura

    @property
    def altura(self):
        return self._altura 

    @altura.setter
    def altura (self,valor):
        if not isinstance(valor,float) and not isinstance(valor,int):
            raise ValueError("O valor da altura deve ser um número")
        if valor < 0:
            raise ValueError("Valor inválido para a altura")
        else:
            self._altura = valor

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base (self,valor):
        if not isinstance(valor,float) and not isinstance(valor,int):
                    raise ValueError("O valor da base deve ser um número")
        if valor < 0:
            raise ValueError("Valor inválido para a base")
        else:
            self._base = valor

    @property
    def area(self):
        area = self._base * self._altura
        return area

    @area.setter
    def area(self):
         raise PermissionError("A área não pode ser configurada desse jeito")

    @property 
    def medidas(self):
        return f"Base = {self.base} \nAltura = {self.altura} \nÁrea = {self.area}"

    @medidas.setter
    def medidas(self,valores:tuple):
        if len(valores) != 2:
             raise SyntaxError ("Informe uma tupla com apenas dois valores numéricos")
        
        if isinstance(valores[0],float) or isinstance(valores[0],int):
             self.base = valores[0]
        else:
             raise TypeError("A base deve ser um número")
        
        if isinstance(valores[1],float) or isinstance(valores[1],int):
                     self.altura = valores[1]
        else:
            raise TypeError("A altura deve ser um número")