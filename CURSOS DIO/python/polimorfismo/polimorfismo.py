class Passaro:
    def voar(self):
        print("Voando")


class Pardal(Passaro):
    def voar(self):
        super().voar()
    


class Avestruz(Passaro):
    def voar(self):
        print("Aveztruz não voa.")

#  FIXME: exemplo ruim do uso de herança
# class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")
    
#Todo objeto tem que ter o método voar implementado
def plano_voo(obj):
    obj.voar()

p1=Pardal()
p2=Avestruz()

plano_voo(p1)
plano_voo(p2)