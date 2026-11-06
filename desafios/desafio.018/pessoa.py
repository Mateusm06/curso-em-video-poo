from abc import ABC

class Pessoa(ABC):
    def __init__(self,nome, nascimento = None):
        self._nome = nome
        self.nascimento = nascimento

    @property 
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,novo_nome):
        self._nome = novo_nome

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self,ano):
        if ano >= 1926 and ano <= 2026:
            self._nascimento = ano
        else:
            raise ValueError(f"Ano {ano} é inválido")

    @property
    def idade(self):
        idade = 2026 - self._nascimento
        return idade

    @idade.setter
    def idade(self,valor):
        raise PermissionError("Para alterar a idade, mude a sua data de nascimento")

class Aluno(Pessoa):
    cursos_oficiais = ["ADM", "ADS", "ENG", "CONT"]
    def __init__(self, nome= None, nascimento= None, curso= None):
        super().__init__(nome, nascimento)
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self,nome):
        if nome not in self.cursos_oficiais:
            raise ValueError("Esse curso não faz parte dos cursos oficiais")
        else:
            self._curso = nome

    def add_curso(self,curso):
        if curso not in self.cursos_oficiais:
            self.cursos_oficiais.append(curso)
