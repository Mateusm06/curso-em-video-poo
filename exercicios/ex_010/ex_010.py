class Avaliacao:

    def __init__(self,nome,disciplina,nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota # Atributo protegido

    # Criando atributo validável
    @property
    def nota(self): # Getter
        return self._nota

    @nota.setter
    def nota(self,valor): # Setter
        if valor >= 0 and valor <= 10:
            self._nota = valor
        else:
            print("Nota inválida")