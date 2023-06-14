from abc import ABC, abstractclassmethod, abstractmethod
from datetime import datetime


class Cliente:
    def __init__(self,endereco):
        self.endereco=endereco
        self.contas=[]

    def realizar_transacao(self,conta,transacao):
        transacao.registrar(conta)

    def adicionar_conta(self,conta):
        self.contas.append(conta)

    
class PessoaFisica(Cliente):
    def __init__(self,nome,data_nascimento,cpf, endereco):
        super().__init__(endereco)
        self.nome=nome
        self.data_nascimento=data_nascimento
        self.cpf=cpf

class Conta:
    def __init__(self,saldo,numero,agencia,cliente):
        self._saldo=saldo
        self._numero=numero
        self._agencia=agencia
        self._cliente=cliente
        self.historico=Historico()

    @classmethod
    def nova_conta(cls,cliente,numero):
        return(cls,numero,cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero



class ContaCorrente(Conta):
    pass

class Historico:
    pass

class Transacao(ABC):
    pass

class Saque(Transacao):
    pass

class Deposito(Transacao):
    pass

