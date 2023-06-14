class Veiculo:
    def __init__(self,cor,placa,numero_rodas):
        self.cor=cor
        self.placa=placa
        self.numero_rodas=numero_rodas

    def ligar_motor(self):
        print("Ligando motor...")

class Motocicleta(Veiculo):
    #Herdou tudo dos métodos de veículo
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas,abastecido=False):
        super().__init__(cor, placa, numero_rodas)
        self.abastecido=abastecido
    def abastecido_carga(self):
        print(f"{'Já' if self.abastecido else 'Não'} recebeu aquilo a ser transportado.")

moto=Motocicleta("Branca","CGI-1570",2)
print(moto.ligar_motor())

carro=Carro("Azul","aaa-1111",4)
carro.ligar_motor()

caminhao=Caminhao("Preto","abd-1234",12,True)
print(caminhao.ligar_motor())#Exibe duas mensagens, pois ele imprime aquilo que foi retornado e executa a função.
caminhao.abastecido_carga()