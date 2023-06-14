class Conta:
    def __init__(self,numero_agencia,saldo=0):
        self._saldo=saldo
        self.numero_agencia=numero_agencia

    def depositar(self,valor):
        # ...
        self._saldo+=valor

    def sacar(self,valor):
         # ...
         self._saldo-=valor

    def mostrar_saldo(self):
        # ...
        return self._saldo

conta=Conta("100",2)
#conta._saldo+=100#Não se deve fazer isso
'''conta.depositar(12,2)
print(conta._saldo)'''#Não há garantia de que não haverá acesso ao atributo, mas devemos seguir aquilo que foi convencionado
print(conta.mostrar_saldo())