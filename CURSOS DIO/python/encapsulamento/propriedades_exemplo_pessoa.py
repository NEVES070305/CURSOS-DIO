class Pessao:
    def __init__(self,nome,ano_nascimento):
        self._nome=nome
        self._ano_nascimento=ano_nascimento

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual=2023
        return _ano_atual-self._ano_nascimento
    
pessoa=Pessao("Guilherme",2005)
print(f"NOME: {pessoa.nome}, tem a idade {pessoa.idade}")