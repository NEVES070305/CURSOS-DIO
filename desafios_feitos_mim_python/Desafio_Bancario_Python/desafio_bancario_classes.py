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
        self._historico=Historico()

    @classmethod
    def nova_conta(cls,cliente,numero):
        return(cls,numero,cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self,valor):
        saldo=self.saldo
        excedeu_saldo=valor>saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor>0:
            self._saldo-=valor
            print("\nSaque realizado com sucesso!")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False
    





class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente,limite=500,limite_saques=3):
        super().__init__(saldo, numero, agencia, cliente)
        self.limite=limite
        self.limite_saques=limite_saques

    def sacar(self,valor):
        numero_saques=len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"]==Saque.__name__]
        )

class Historico:
    pass

class Transacao(ABC):
    pass

class Saque(Transacao):
    pass

class Deposito(Transacao):
    pass


